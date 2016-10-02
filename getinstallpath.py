#########################################################################################
#      This file is part of mindwave-supercollider.                                     #
#                                                                                       #
#      mindwave-supercollider is free software: you can redistribute it and/or modify   #
#      it under the terms of the GNU General Public License as published by             #
#      the Free Software Foundation, either version 3 of the License, or                #
#      (at your option) any later version.                                              #
#                                                                                       #
#      mindwave-supercollider is distributed in the hope that it will be useful,        #
#      but WITHOUT ANY WARRANTY; without even the implied warranty of                   #
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                    #
#      GNU General Public License for more details.                                     #
#                                                                                       #
#      You should have received a copy of the GNU General Public License                #
#      along with mindwave-supercollider.  If not, see <http://www.gnu.org/licenses/>.  #
#########################################################################################

import os.path
import sys
def getInstallPath():
    """
    function that returns the directory where the script is located
    """
    thePath = os.path.dirname(sys.argv[0])
    if thePath:
        thePath += os.sep
    else:
        thePath = "./"
    return os.path.abspath(thePath)

