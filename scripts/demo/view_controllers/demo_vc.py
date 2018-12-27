#
#  This file is part of Permafrost Engine. 
#  Copyright (C) 2018 Eduard Permyakov 
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
from constants import *
import view_controller as vc

class DemoVC(vc.ViewController):

    def __init__(self, view):
        self.__view = view
        self.__view.fac_names = [fac["name"] for fac in pf.get_factions_list()]
        assert len(self.__view.fac_names) >= 2
        self.__view.active_fac_idx = 1

    def __on_controlled_faction_chagned(self, event):
        pf.clear_unit_selection()
        for i in range(len(pf.get_factions_list())):
            pf.set_faction_controllable(i, False) 
        pf.set_faction_controllable(event, True)

    def activate(self):
        pf.register_event_handler(EVENT_CONTROLLED_FACTION_CHANGED, DemoVC.__on_controlled_faction_chagned, self)
        self.__view.show()

    def deactivate(self):
        self.__view.hide()
        pf.unregister_event_handler(EVENT_CONTROLLED_FACTION_CHANGED, DemoVC.__on_controlled_faction_chagned)

