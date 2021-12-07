# Discord: A-Dawg#0001 (AE)
# Supports: Forza Horizon 5
# Offically (OTHER v1.405.2.0, MS STORE v3.414.967.0, STEAM v1.414.967.0)
# Unofficially (most versions should work)
# License: MIT
# Year: 2021

import ctypes
from ctypes import wintypes
from numpy import longlong
import win32process
import sys
import struct

ERROR_PARTIAL_COPY = 0x012B
PROCESS_VM_READ = 0x0010
PROCESS_ALL_ACCESS = 0x1F0FFF
SIZE_T = ctypes.c_size_t
PSIZE_T = ctypes.POINTER(SIZE_T)

hProcess = None
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

def _check_zero(result, func, args):
    if not result:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

kernel32.OpenProcess.errcheck = _check_zero
kernel32.OpenProcess.restype = wintypes.HANDLE
kernel32.OpenProcess.argtypes = (
    wintypes.DWORD, # _In_ dwDesiredAccess
    wintypes.BOOL,  # _In_ bInheritHandle
    wintypes.DWORD) # _In_ dwProcessId

kernel32.ReadProcessMemory.errcheck = _check_zero
kernel32.ReadProcessMemory.argtypes = (
    wintypes.HANDLE,  # _In_  hProcess
    wintypes.LPCVOID, # _In_  lpBaseAddress
    wintypes.LPVOID,  # _Out_ lpBuffer
    SIZE_T,           # _In_  nSize
    PSIZE_T)          # _Out_ lpNumberOfBytesRead

kernel32.WriteProcessMemory.errcheck = _check_zero
kernel32.WriteProcessMemory.argtypes = (
    wintypes.HANDLE,  # _In_  hProcess
    wintypes.LPCVOID, # _In_  lpBaseAddress
    wintypes.LPVOID,  # _Out_ lpBuffer
    SIZE_T,           # _In_  nSize
    PSIZE_T)          # _Out_ lpNumberOfBytesWritten

kernel32.CloseHandle.argtypes = (wintypes.HANDLE,)

def is_64bit():
    return struct.calcsize("P") == 8

def get_base_address(pid):
    hProcess = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    modules = win32process.EnumProcessModules(hProcess)
    kernel32.CloseHandle(hProcess)
    return modules[0]

def read_process_memory(pid, address, size):
    global hProcess
    buf = (ctypes.c_char * size)()
    nread = SIZE_T()
    if hProcess is None:
        hProcess = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    try:
        kernel32.ReadProcessMemory(hProcess, address, buf, size,
            ctypes.byref(nread))
    except WindowsError as e:
        # if not e.winerror != ERROR_PARTIAL_COPY:
        #     raise
        pass
    return buf[:nread.value]

def write_process_memory(pid, address, buf):
    global hProcess
    nwritten = SIZE_T()
    if hProcess is None:
        hProcess = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    try:
        kernel32.WriteProcessMemory(hProcess, address, buf, len(buf),
            ctypes.byref(nwritten))
    except WindowsError as e:
        raise
    return

def scan_block(pid, start_address, block_size, scan_for):
    memory = read_process_memory(pid, start_address, block_size)
    return memory.find(scan_for)

def dereference_pointer(pid, pointer_address):
    address_bytes = read_process_memory(pid, pointer_address, 8)
    return int.from_bytes(address_bytes, byteorder=sys.byteorder)

def read_int(pid, int_address):
    int_bytes = read_process_memory(pid, int_address, 4)
    return int.from_bytes(int_bytes, byteorder=sys.byteorder)

def read_long(pid, int_address):
    long_bytes = read_process_memory(pid, int_address, 8)
    return int.from_bytes(long_bytes, byteorder=sys.byteorder)