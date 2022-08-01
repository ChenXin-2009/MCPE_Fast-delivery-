# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi
import time
from mod.server.system.serverSystem import ServerSystem

ServerSystem = serverApi.GetServerSystemCls()


class C_Xin_kscsMod_ServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        # 我们通过查阅文档可知，服务端的ServerChatEvent事件可以做到响应玩家发送聊天栏信息，于是我们为其设置事件监听。
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.on_chat)

    def on_chat(self, event):
        # 下面是设置玩家ID为变量
        player_id = event['playerId']
        print("<<<<<<<<<<<<<<<<<<<===================", "player_id:", player_id,
              "========================>>>>>>>>>>>>>>>>")
        # 下面是设置玩家消息为变量
        message = event['message']

        # 下面是设置生物群系字典
        # 这里将采用遍历生物群系键的方法获取生物群系的英文名，然后加入/tptobiome @s XXX 中实现生物群系的传送
        biomes = {
            "传送至竹林": "bamboo_jungle",
            "传送至竹林丘陵": "bamboo_jungle_hills",
            "传送至玄武岩三角洲": "basalt_deltas",
            "传送至沙滩": "beach",
            "传送至桦木森林": "birch_forest",
            "传送至桦木森林丘陵": "birch_forest_hills",
            "传送至高大桦木丘陵": "birch_forest_hills_mutated",
            "传送至原始桦木森林": "birch_forest_mutated",
            "传送至积雪的沙滩": "cold_beach",
            "传送至冷水海洋": "cold_ocean",
            "传送至积雪的针叶林": "cold_taiga",
            "传送至积雪的针叶林丘陵": "cold_taiga_hills",
            "传送至积雪的针叶林山地": "cold_taiga_mutated",
            "传送至绯红森林": "crimson_forest",
            "传送至冷水深海": "deep_cold_ocean",
            "传送至深暗之域": "deep_dark",
            "传送至冰冻深海": "deep_frozen_ocean",
            "传送至温水深海": "deep_lukewarm_ocean",
            "传送至深海": "deep_ocean",
            "传送至沙漠": "desert",
            "传送至沙漠丘陵": "desert_hills",
            "传送至沙漠湖泊": "desert_mutated",
            "传送至溶洞": "dripstone_caves",
            "传送至风袭丘陵": "extreme_hills",
            "传送至山地边缘": "extreme_hills_edge",
            "传送至风袭沙砾丘陵": "extreme_hills_mutated",
            "传送至风袭森林": "extreme_hills_plus_trees",
            "传送至沙砾山地": "extreme_hills_plus_trees_mutated",
            "传送至繁花森林": "flower_forest",
            "传送至森林": "forest",
            "传送至繁茂的丘陵": "forest_hills",
            "传送至冻洋": "frozen_ocean",
            "传送至冰封山峰": "frozen_peaks",
            "传送至冻河": "frozen_river",
            "传送至雪林": "grove",
            "传送至下界荒地": "hell",
            "传送至雪山": "ice_mountains",
            "传送至积雪的平原": "ice_plains",
            "传送至冰刺平原": "ice_plains_spikes",
            "传送至尖峭山峰": "jagged_peaks",
            "传送至丛林": "jungle",
            "传送至稀疏的丛林": "jungle_edge",
            "传送至丛林边缘变种": "jungle_edge_mutated",
            "传送至丛林丘陵": "jungle_hills",
            "传送至丛林变种": "jungle_mutated",
            "传送至冻洋（旧版）": "legacy_frozen_ocean",
            "传送至温水海洋": "lukewarm_ocean",
            "传送至繁茂洞穴": "lush_caves",
            "传送至红树林沼泽": "mangrove_swamp",
            "传送至草甸": "meadow",
            "传送至原始松木针叶林": "mega_taiga",
            "传送至巨型针叶林丘陵": "mega_taiga_hills",
            "传送至恶地": "mesa",
            "传送至被风蚀的恶地": "mesa_bryce",
            "传送至恶地高原": "mesa_plateau",
            "传送至恶地高原变种": "mesa_plateau_mutated",
            "传送至繁茂的恶地高原": "mesa_plateau_stone",
            "传送至繁茂的恶地高原变种": "mesa_plateau_stone_mutated",
            "传送至蘑菇岛": "mushroom_island",
            "传送至蘑菇岛岸": "mushroom_island_shore",
            "传送至海洋": "ocean",
            "传送至平原": "plains",
            "传送至巨型云杉针叶林丘陵": "redwood_taiga_hills_mutated",
            "传送至原始云杉针叶林": "redwood_taiga_mutated",
            "传送至河流": "river",
            "传送至黑森林": "roofed_forest",
            "传送至黑森林丘陵": "roofed_forest_mutated",
            "传送至热带草原": "savanna",
            "传送至风袭热带草原": "savanna_mutated",
            "传送至热带高原": "savanna_plateau",
            "传送至破碎的热带高原": "savanna_plateau_mutated",
            "传送至积雪的山坡": "snowy_slopes",
            "传送至灵魂沙峡谷": "soulsand_valley",
            "传送至石岸": "stone_beach",
            "传送至裸岩山峰": "stony_peaks",
            "传送至向日葵平原": "sunflower_plains",
            "传送至沼泽": "swampland",
            "传送至沼泽丘陵": "swampland_mutated",
            "传送至针叶林": "taiga",
            "传送至针叶林丘陵": "taiga_hills",
            "传送至针叶林山地": "taiga_mutated",
            "传送至末地": "the_end",
            "传送至暖水海洋": "warm_ocean",
            "传送至诡异森林": "warped_forest",
        }

        for i in biomes:
            if message == i:
                comp = serverApi.GetEngineCompFactory().CreateCommand(player_id)
                comp.SetCommand("/tptobiome @s " + biomes[i])  # 传送指令

        locate = {
            "传送至末地城": "EndCity",
            "传送至下界要塞": "Fortress",
            "传送至废弃矿井": "Mineshaft",
            "传送至海底神殿": "Monument",
            "传送至要塞": "Stronghold",
            "传送至特殊建筑": "Temple",  # 因为我也不知道为什么网易那啥Api接口的StructureFeatureType里的这个参数把沙漠神殿/雪屋/丛林神庙/女巫小屋合在一起了
            "传送至村庄": "Village",
            "传送至林地府邸": "WoodlandMansion",
            "传送至沉船": "Shipwreck",
            "传送至埋藏的宝藏": "BuriedTreasure",
            "传送至水下遗迹": "Ruins",
            "传送至掠夺者前哨站": "PillagerOutpost",
            "传送至废弃传送门": "RuinedPortal",
            "传送至堡垒遗迹": "Bastion",
        }
        for j in locate:
            if message == j:
                comp = serverApi.GetEngineCompFactory().CreateDimension(player_id)
                DimensionId = comp.GetEntityDimensionId()
                print("================================dimensionId================================", DimensionId)
                # 上面是获取玩家所在维度
                comp = serverApi.GetEngineCompFactory().CreatePos(player_id)
                Pos = comp.GetPos()
                print("===================================pos=============================", Pos)
                print Pos
                # 上面是获取玩家位置
                if locate[j] == "EndCity":  # 1
                    comp = serverApi.GetEngineCompFactory().CreateFeature(player_id)
                    MinecraftEnumPos = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.EndCity, DimensionId, Pos)
                    print("=================================minecraftEnumPos===============================", MinecraftEnumPos)
                elif locate[j] == "Fortress":  # 2
                    comp = serverApi.GetEngineCompFactory().CreateFeature(player_id)
                    MinecraftEnumPos = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.Fortress, DimensionId, Pos)
                    print("=================================minecraftEnumPos===============================", MinecraftEnumPos)
                elif locate[j] == "Mineshaft":  # 3
                    comp = serverApi.GetEngineCompFactory().CreateFeature(player_id)
                    MinecraftEnumPos = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.Mineshaft, DimensionId, Pos)
                    print("=================================minecraftEnumPos===============================", MinecraftEnumPos)
                elif locate[j] == "Monument":  # 4
                    comp = serverApi.GetEngineCompFactory().CreateFeature(player_id)
                    MinecraftEnumPos = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.Monument, DimensionId, Pos)
                    print("=================================minecraftEnumPos===============================", MinecraftEnumPos)
                elif locate[j] == "Stronghold":  # 5
                    comp = serverApi.GetEngineCompFactory().CreateFeature(player_id)
                    MinecraftEnumPos = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.Stronghold, DimensionId, Pos)
                    print("=================================minecraftEnumPos===============================", MinecraftEnumPos)
                elif locate[j] == "Temple":  # 6
                    comp = serverApi.GetEngineCompFactory().CreateFeature(player_id)
                    MinecraftEnumPos = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.Temple, DimensionId, Pos)
                    print("=================================minecraftEnumPos===============================", MinecraftEnumPos)
                elif locate[j] == "Village":  # 7
                    comp = serverApi.GetEngineCompFactory().CreateFeature(player_id)
                    MinecraftEnumPos = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.Village, DimensionId, Pos)
                    print("=================================minecraftEnumPos===============================", MinecraftEnumPos)
                elif locate[j] == "WoodlandMansion":  # 8
                    comp = serverApi.GetEngineCompFactory().CreateFeature(player_id)
                    MinecraftEnumPos = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.WoodlandMansion, DimensionId, Pos)
                    print("=================================minecraftEnumPos===============================", MinecraftEnumPos)
                elif locate[j] == "Shipwreck":  # 9
                    comp = serverApi.GetEngineCompFactory().CreateFeature(player_id)
                    MinecraftEnumPos = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.Shipwreck, DimensionId, Pos)
                    print("=================================minecraftEnumPos===============================", MinecraftEnumPos)
                elif locate[j] == "BuriedTreasure":  # 10
                    comp = serverApi.GetEngineCompFactory().CreateFeature(player_id)
                    MinecraftEnumPos = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.BuriedTreasure, DimensionId, Pos)
                    print("=================================minecraftEnumPos===============================", MinecraftEnumPos)
                elif locate[j] == "Ruins":  # 11
                    comp = serverApi.GetEngineCompFactory().CreateFeature(player_id)
                    MinecraftEnumPos = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.Ruins, DimensionId, Pos)
                    print("=================================minecraftEnumPos===============================", MinecraftEnumPos)
                elif locate[j] == "PillagerOutpost":  # 12
                    comp = serverApi.GetEngineCompFactory().CreateFeature(player_id)
                    MinecraftEnumPos = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.PillagerOutpost, DimensionId, Pos)
                    print("=================================minecraftEnumPos===============================", MinecraftEnumPos)
                elif locate[j] == "RuinedPortal":  # 13
                    comp = serverApi.GetEngineCompFactory().CreateFeature(player_id)
                    MinecraftEnumPos = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.RuinedPortal, DimensionId, Pos)
                    print("=================================minecraftEnumPos===============================", MinecraftEnumPos)
                elif locate[j] == "Bastion":  # 14
                    comp = serverApi.GetEngineCompFactory().CreateFeature(player_id)
                    MinecraftEnumPos = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.Bastion, DimensionId, Pos)
                    print("=================================minecraftEnumPos===============================", MinecraftEnumPos)

                if MinecraftEnumPos == None:
                    comp = serverApi.GetEngineCompFactory().CreateCommand(player_id)
                    comp.SetCommand("say 无法找到该建筑")

                comp = serverApi.GetEngineCompFactory().CreateCommand(player_id)
                comp.SetCommand("/tp @s " + str(MinecraftEnumPos[0]) + " " + "200" + " " + str(MinecraftEnumPos[1]))  # 传送指令
                comp = serverApi.GetEngineCompFactory().CreateEffect(player_id)
                res = comp.AddEffectToEntity("resistance", 8, 254, False)

    def Destroy(self):
        pass
