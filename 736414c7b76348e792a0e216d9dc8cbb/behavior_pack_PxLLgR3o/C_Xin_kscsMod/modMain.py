# -*- coding: utf-8 -*-

from common.mod import Mod
import mod.server.extraServerApi as serverApi

@Mod.Binding(name="C_Xin_kscsMod", version="0.0.1")
class C_Xin_kscsMod(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def C_Xin_kscsModServerInit(self):
        serverApi.RegisterSystem("C_Xin_kscsMod", "C_Xin_kscsMod_System", "C_Xin_kscsMod.C_Xin_kscsMod_ServerSystem.C_Xin_kscsMod_ServerSystem")
        print("======================================================================================\n")
        print("==<<<<====<<<<>>>>>>>>=====C_Xin_kscsModServerInit调用成功！！！===<<<<=====<<<<>>>>>>>>")
        print("======================================================================================\n")

    @Mod.DestroyServer()
    def C_Xin_kscsModServerDestroy(self):
        pass

    @Mod.InitClient()
    def C_Xin_kscsModClientInit(self):
        pass

    @Mod.DestroyClient()
    def C_Xin_kscsModClientDestroy(self):
        pass
