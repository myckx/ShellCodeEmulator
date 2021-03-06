#!/usr/bin/env python
# pylint: disable=unused-wildcard-import

class Tool:
    @staticmethod
    def dump_hex(bytes):
        line = ''
        count = 0
        for ch in bytes:
            if isinstance(ch, str):
                ch = ord(ch)
            line += '%.2x ' % ch
            if count % 0x10 == 0xf:
                line += '\n'
            count += 1
            
        return line
