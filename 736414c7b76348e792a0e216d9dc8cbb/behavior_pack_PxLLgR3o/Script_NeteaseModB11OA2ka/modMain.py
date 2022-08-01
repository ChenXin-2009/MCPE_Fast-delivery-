# -*- coding: utf-8 -*-

from common.mod import Mod


@Mod.Binding(name="Script_NeteaseModB11OA2ka", version="0.0.1")
class Script_NeteaseModB11OA2ka(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModB11OA2kaServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModB11OA2kaServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModB11OA2kaClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModB11OA2kaClientDestroy(self):
        pass
