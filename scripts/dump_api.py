#
#  This file is part of Permafrost Engine. 
#  Copyright (C) 2018-2020 Eduard Permyakov 
#
#  Permafrost Engine is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Permafrost Engine is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
#  Linking this software statically or dynamically with other modules is making 
#  a combined work based on this software. Thus, the terms and conditions of 
#  the GNU General Public License cover the whole combination. 
#  
#  As a special exception, the copyright holders of Permafrost Engine give 
#  you permission to link Permafrost Engine with independent modules to produce 
#  an executable, regardless of the license terms of these independent 
#  modules, and to copy and distribute the resulting executable under 
#  terms of your choice, provided that you also meet, for each linked 
#  independent module, the terms and conditions of the license of that 
#  module. An independent module is a module which is not derived from 
#  or based on Permafrost Engine. If you modify Permafrost Engine, you may 
#  extend this exception to your version of Permafrost Engine, but you are not 
#  obliged to do so. If you do not wish to do so, delete this exception 
#  statement from your version.
#

import pf
import types

TAB_WIDTH = 4

star_border = '*' * 80
line_border = '-' * 80
tab = ' ' * TAB_WIDTH

def indented_border(ntabs, char='*'):
    head = ntabs * tab
    tail = char * (80 - (ntabs * TAB_WIDTH))
    return head + tail

def wrap_text(text, width, indent):
    assert indent < width
    ret = ''
    read = 0
    while read < len(text):
        line_chars = 0
        while line_chars < indent:
            ret += ' '
            line_chars += 1
        while line_chars < width and read < len(text):
            ret += text[read]
            line_chars += 1
            read += 1
        if read < len(text):
            ret += '\n'
    return ret

print star_border
print "Permafrost Engine Python API documentation"
print "Module: {0}".format(pf.__name__)
print star_border
print
print "This file is generated by the script: {0}.".format(__file__)
print "Use this script as the engine argument to generate up-to-date API documentation."
print
print star_border
print "BUILT-IN FUNCTIONS"
print star_border
print

for func in [getattr(pf, attr) for attr in dir(pf) if isinstance(getattr(pf, attr), types.BuiltinFunctionType)]:
    print tab + "[{0}]".format(func.__name__)
    print indented_border(1, char='-')
    print "{0}".format(wrap_text(func.__doc__, 80, 1 * TAB_WIDTH))
    print

print star_border
print "BUILT-IN CLASSES"
print star_border
print

for cls in [getattr(pf, attr) for attr in dir(pf) if isinstance(getattr(pf, attr), types.TypeType)]:
    print tab + "[{0}]".format(cls.__name__)
    print indented_border(1, char='-')
    print "{0}".format(wrap_text(cls.__doc__, 80, 1 * TAB_WIDTH))
    print

    fields = [getattr(cls, attr) for attr in dir(cls) if isinstance(getattr(cls, attr), types.MemberDescriptorType) \
                                                      or isinstance(getattr(cls, attr), types.GetSetDescriptorType)]
    if len(fields) > 0:
        print indented_border(2, char='*')
        print 2*tab + "MEMBERS"
        print indented_border(2, char='*')
    for field in fields:
        print 2*tab + "[{0}]".format(field.__name__)
        print "{0}".format(wrap_text(field.__doc__, 80, 2 * TAB_WIDTH))
        print

    methods = [getattr(cls, attr) for attr in dir(cls) if callable(getattr(cls, attr))
                                                       and attr not in dir(object)
                                                       and not isinstance(getattr(cls, attr), types.BuiltinMethodType)]
                                                       
    if len(methods) > 0:
        print indented_border(2, char='*')
        print 2*tab + "METHODS"
        print indented_border(2, char='*')
    for method in methods:
        print 2*tab + "[{0}]".format(method.__name__)
        print "{0}".format(wrap_text(method.__doc__, 80, 2 * TAB_WIDTH))
        print

print star_border
print "BUILT-IN CONSTANTS"
print star_border 
print

for const in [attr for attr in dir(pf) if (isinstance(getattr(pf, attr), types.IntType)
                                       or isinstance(getattr(pf, attr), types.LongType)
                                       or isinstance(getattr(pf, attr), types.FloatType)
                                       or isinstance(getattr(pf, attr), types.StringType)
                                       or isinstance(getattr(pf, attr), types.UnicodeType))
                                       and not attr.startswith('__')]:
    print(tab + "{0} {1}".format(const, getattr(pf, const)))

def on_tick(user, event):
    pf.global_event(pf.SDL_QUIT, None)

pf.register_event_handler(pf.EVENT_UPDATE_START, on_tick, None)

