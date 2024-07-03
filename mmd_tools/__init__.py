# -*- coding: utf-8 -*-
# WARNING: This is a software crutch))
# Copyright 2012 MMD Tools authors
# This file is part of MMD Tools.

# MMD Tools is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# MMD Tools is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
bl_info = {
    "name": "mmd_tools",
    "author": "sugiany",
    "version": (2, 10, 4),
    "blender": (2, 93, 0),
    "location": "View3D > Sidebar > MMD Tools Panel",
    "description": "Utility tools for MMD model editing. (UuuNyaa's forked version)",
    "warning": "",
    "doc_url": "https://mmd-blender.fandom.com/wiki/MMD_Tools",
    "wiki_url": "https://mmd-blender.fandom.com/wiki/MMD_Tools",
    "tracker_url": "https://github.com/UuuNyaa/blender_mmd_tools/issues",
    "category": "Object",
}

import os

PACKAGE_NAME = bl_info['name']
PACKAGE_PATH = os.path.dirname(__file__)

with open(os.path.join(PACKAGE_PATH, "blender_manifest.toml"), "rb") as f:
    import tomllib

    manifest = tomllib.load(f)
    MMD_TOOLS_VERSION = manifest["version"]


from . import auto_load

auto_load.init(PACKAGE_NAME)


def register():
    import bpy

    from . import handlers

    auto_load.register()

    # pylint: disable=import-outside-toplevel
    from .m17n import translation_dict

    bpy.app.translations.register(PACKAGE_NAME, translation_dict)

    handlers.MMDHanders.register()


def unregister():
    import bpy

    from . import handlers

    handlers.MMDHanders.unregister()

    bpy.app.translations.unregister(PACKAGE_NAME)

    auto_load.unregister()


if __name__ == "__main__":
    register()
