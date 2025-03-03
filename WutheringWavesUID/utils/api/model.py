from typing import Any, Dict, List, Literal, Optional, Union

from msgspec import UNSET, Struct, UnsetType, field
from pydantic import BaseModel, RootModel


class GeneralGeetestData(Struct):
    geetest_challenge: str
    geetest_seccode: str
    geetest_validate: str


class GeneralV1SendPhoneCodeRequest(Struct):
    phone: str
    type: int
    captcha: Union[GeneralGeetestData, UnsetType] = field(default=UNSET)


class EnergyData(BaseModel):
    """结晶波片"""

    name: str
    img: str
    refreshTimeStamp: int
    cur: int
    total: int


class LivenessData(BaseModel):
    """活跃度"""

    name: str
    img: str
    cur: int
    total: int


class BattlePassData(BaseModel):
    """电台"""

    name: str
    cur: int
    total: int


class DailyData(BaseModel):
    """每日数据"""

    gameId: int
    userId: int
    serverId: str
    roleId: str
    roleName: str
    signInTxt: str
    hasSignIn: bool
    energyData: EnergyData
    livenessData: LivenessData
    battlePassData: List[BattlePassData]


class Role(BaseModel):
    roleId: int
    level: int
    breach: Optional[int] = None
    roleName: str
    roleIconUrl: Optional[str]
    rolePicUrl: Optional[str]
    starLevel: int
    attributeId: int
    attributeName: Optional[str]
    weaponTypeId: int
    weaponTypeName: Optional[str]
    acronym: str
    # mapRoleId: int | None


class RoleList(BaseModel):
    roleList: List[Role]


class Box(BaseModel):
    boxName: str
    num: int


class Box2(BaseModel):
    name: str
    num: int


class AccountBaseInfo(BaseModel):
    """账户基本信息"""

    name: str  # 名字
    id: int  # 特征码
    creatTime: Optional[int] = None  # 创建时间 ms
    activeDays: Optional[int] = None  # 活跃天数
    level: Optional[int] = None  # 等级
    worldLevel: Optional[int] = None  # 世界等级
    roleNum: Optional[int] = None  # 角色数量
    bigCount: Optional[int] = None  # 大型信标解锁数
    smallCount: Optional[int] = None  # 小型信标解锁数
    achievementCount: Optional[int] = None  # 成就数量
    achievementStar: Optional[int] = None  # 成就星数
    boxList: Optional[List[Optional[Box]]] = None  # 宝箱
    treasureBoxList: Optional[List[Optional[Box2]]] = None  # 宝箱
    weeklyInstCount: Optional[int] = None  # 周本次数
    weeklyInstCountLimit: Optional[int] = None  # 周本限制次数
    storeEnergy: Optional[int] = None  # 结晶单质数量
    storeEnergyLimit: Optional[int] = None  # 结晶单质限制

    @property
    def is_full(self):
        """完整数据，没有隐藏库街区数据"""
        return isinstance(self.creatTime, int)


class Chain(BaseModel):
    name: Optional[str]
    order: int
    description: Optional[str]
    iconUrl: Optional[str]
    unlocked: bool


class Weapon(BaseModel):
    weaponId: int
    weaponName: str
    weaponType: int
    weaponStarLevel: int
    weaponIcon: Optional[str]
    weaponEffectName: Optional[str]
    # effectDescription: Optional[str]


class WeaponData(BaseModel):
    weapon: Weapon
    level: int
    breach: Optional[int] = None
    resonLevel: Optional[int]


class PhantomProp(BaseModel):
    phantomPropId: int
    name: str
    phantomId: int
    quality: int
    cost: int
    iconUrl: str
    skillDescription: Optional[str]


class FetterDetail(BaseModel):
    groupId: int
    name: str
    iconUrl: Optional[str]
    num: int
    firstDescription: Optional[str]
    secondDescription: Optional[str]


class Props(BaseModel):
    attributeName: str
    iconUrl: Optional[str] = None
    attributeValue: str


class EquipPhantom(BaseModel):
    phantomProp: PhantomProp
    cost: int
    quality: int
    level: int
    fetterDetail: FetterDetail
    mainProps: Optional[List[Props]] = None
    subProps: Optional[List[Props]] = None

    def get_props(self):
        props = []
        if self.mainProps:
            props.extend(self.mainProps)
        if self.subProps:
            props.extend(self.subProps)

        return props


class EquipPhantomData(BaseModel):
    cost: int
    equipPhantomList: Union[List[Optional[EquipPhantom]], None, List[None]] = None


class Skill(BaseModel):
    id: int
    type: str
    name: str
    description: str
    iconUrl: str


class SkillData(BaseModel):
    skill: Skill
    level: int


class RoleDetailData(BaseModel):
    role: Role
    level: int
    chainList: List[Chain]
    weaponData: WeaponData
    phantomData: Optional[EquipPhantomData] = None
    skillList: List[SkillData]

    def get_chain_num(self):
        """获取命座数量"""
        num = 0
        for index, chain in enumerate(self.chainList):
            if chain.unlocked:
                num += 1
        return num

    def get_chain_name(self):
        n = self.get_chain_num()
        return f"{['零', '一', '二', '三', '四', '五', '六'][n]}链"

    def get_skill_level(
        self,
        skill_type: Literal["常态攻击", "共鸣技能", "共鸣解放", "变奏技能", "共鸣回路"],
    ):
        skill_level = 1
        _skill = next(
            (skill for skill in self.skillList if skill.skill.type == skill_type), None
        )
        if _skill:
            skill_level = _skill.level - 1
        return skill_level

    def get_skill_list(self):
        sort = ["常态攻击", "共鸣技能", "共鸣回路", "共鸣解放", "变奏技能", "延奏技能"]
        return sorted(self.skillList, key=lambda x: sort.index(x.skill.type))


class CalabashData(BaseModel):
    """数据坞"""

    level: Optional[int]  # 数据坞等级
    baseCatch: Optional[str]  # 基础吸收概率
    strengthenCatch: Optional[str]  # 强化吸收概率
    catchQuality: Optional[int]  # 最高可吸收品质
    cost: Optional[int]  # cost上限
    maxCount: Optional[int]  # 声骸收集进度-max
    unlockCount: Optional[int]  # 声骸收集进度-curr
    isUnlock: bool  # 解锁


class KuroRoleInfo(BaseModel):
    """库洛角色信息"""

    id: int
    userId: int
    gameId: int
    serverId: str
    serverName: str
    roleId: str
    roleName: str
    gameHeadUrl: str
    roleNum: int
    achievementCount: int


class GachaLog(BaseModel):
    """抽卡记录"""

    cardPoolType: str
    resourceId: int
    qualityLevel: int
    resourceType: str
    name: str
    count: int
    time: str

    def __hash__(self):
        return hash((self.resourceId, self.time))


# 定义角色模型
class AbyssRole(BaseModel):
    roleId: int
    iconUrl: Optional[str] = None


# 定义楼层模型
class AbyssFloor(BaseModel):
    floor: int
    picUrl: str
    star: int
    roleList: Optional[List[AbyssRole]] = None


# 定义区域模型
class AbyssArea(BaseModel):
    areaId: int
    areaName: str
    star: int
    maxStar: int
    floorList: Optional[List[AbyssFloor]] = None


# 定义难度模型
class AbyssDifficulty(BaseModel):
    difficulty: int
    difficultyName: str
    towerAreaList: List[AbyssArea]


# 定义顶层模型
class AbyssChallenge(BaseModel):
    isUnlock: bool
    seasonEndTime: Optional[int]
    difficultyList: Optional[List[AbyssDifficulty]]


class ChallengeRole(BaseModel):
    roleName: Optional[str]
    roleHeadIcon: Optional[str]
    roleLevel: Optional[int]
    natureId: Optional[int]
    natureIcon: Optional[Any] = None


class Challenge(BaseModel):
    bossId: Optional[Any] = None
    challengeId: Optional[int] = None
    bossHeadIcon: Optional[str] = None
    bossIconUrl: Optional[str] = None
    bossLevel: Optional[int] = None
    bossName: Optional[str] = None
    passTime: Optional[int] = None
    difficulty: Optional[int] = None
    roles: Optional[List[ChallengeRole]] = None


class ChallengeArea(BaseModel):
    areaId: Optional[Any] = None
    areaName: Optional[Any] = None
    challengeInfo: Optional[Dict[str, List[Challenge]]] = None
    open: bool
    wikiUrl: Optional[Any] = None
    isUnlock: bool


class ExploreItem(BaseModel):
    name: str
    progress: int
    type: int


class AreaInfo(BaseModel):
    areaId: int
    areaName: str
    areaProgress: int
    itemList: List[ExploreItem]


class ExploreCountry(BaseModel):
    countryId: int
    countryName: str
    detailPageFontColor: str
    detailPagePic: str
    detailPageProgressColor: str
    homePageIcon: str


class ExploreArea(BaseModel):
    areaInfoList: Union[List[AreaInfo], None] = None
    country: ExploreCountry
    countryProgress: str


class ExploreList(BaseModel):
    """探索度"""

    exploreList: Union[List[ExploreArea], None] = None
    open: bool


class OnlineWeapon(BaseModel):
    """
    {
        "weaponId": 21010011,
        "weaponName": "教学长刃",
        "weaponType": 1,
        "weaponStarLevel": 1,
        "weaponIcon": "https://web-static.kurobbs.com/adminConfig/29/weapon_icon/1716031228478.png",
        "isPreview": false,
        "isNew": false,
        "priority": 1,
        "acronym": "jxcr"
    }
    """

    weaponId: int
    weaponName: str
    weaponType: int
    weaponStarLevel: int
    weaponIcon: str
    isPreview: bool
    isNew: bool
    priority: int
    acronym: str


class OnlineWeaponList(RootModel[List[OnlineWeapon]]):
    def __iter__(self):
        return iter(self.root)


class OnlineRole(BaseModel):
    """
    {
        "roleId": 1102,
        "roleName": "散华",
        "roleIconUrl": "https://web-static.kurobbs.com/adminConfig/98/role_icon/1738924370710.png",
        "starLevel": 4,
        "attributeId": 1,
        "attributeName": null,
        "weaponTypeId": 2,
        "weaponTypeName": "迅刀",
        "acronym": "sh",
        "isPreview": false,
        "isNew": false,
        "priority": 4
    }
    """

    roleId: int
    roleName: str
    roleIconUrl: str
    starLevel: int
    attributeId: int
    attributeName: Optional[str]
    weaponTypeId: int
    weaponTypeName: str
    acronym: str
    isPreview: bool
    isNew: bool
    priority: int


class OnlineRoleList(RootModel[List[OnlineRole]]):
    def __iter__(self):
        return iter(self.root)


class OnlinePhantom(BaseModel):
    """
    {
        "phantomId": 390080005,
        "name": "鸣钟之龟",
        "cost": 4,
        "risk": "海啸级",
        "iconUrl": "https://web-static.kurobbs.com/adminConfig/35/phantom_icon/1716031298428.png",
        "isPreview": false,
        "isNew": false,
        "priority": 104,
        "fetterIds": "8,7",
        "acronym": "mzzg"
    }
    """

    phantomId: int
    name: str
    cost: int
    risk: str
    iconUrl: str
    isPreview: bool
    isNew: bool
    priority: int
    fetterIds: str
    acronym: str


class OnlinePhantomList(RootModel[List[OnlinePhantom]]):
    def __iter__(self):
        return iter(self.root)


class OwnedRoleList(RootModel[List[int]]):
    def __iter__(self):
        return iter(self.root)


class RoleCultivateSkillLevel(BaseModel):
    type: str
    level: int


class RoleCultivateStatus(BaseModel):
    """角色培养状态
    {
        "roleId": 1107,
        "roleName": "珂莱塔",
        "roleLevel": 90,
        "roleBreakLevel": 6,
        "skillLevelList": [{
                "type": "常态攻击",
                "level": 1
        }, {
                "type": "共鸣技能",
                "level": 10
        }, {
                "type": "共鸣解放",
                "level": 10
        }, {
                "type": "变奏技能",
                "level": 6
        }, {
                "type": "共鸣回路",
                "level": 10
        }, {
                "type": "延奏技能",
                "level": 1
        }],
        "skillBreakList": ["2-3", "3-3", "2-1", "2-2", "2-4", "2-5", "3-1", "3-2", "3-4", "3-5"]
    }
    """

    roleId: int
    roleName: str
    roleLevel: int
    roleBreakLevel: int  # 突破等级
    skillLevelList: List[RoleCultivateSkillLevel]
    skillBreakList: List[str]  # 突破技能


class RoleCultivateStatusList(RootModel[List[RoleCultivateStatus]]):
    def __iter__(self):
        return iter(self.root)


class CultivateCost(BaseModel):
    """培养成本
    {
        "id": "2",
        "name": "贝币",
        "iconUrl": "https://web-static.kurobbs.com/gamerdata/calculator/coin.png",
        "num": 4460260,
        "type": 0,
        "quality": 3,
        "isPreview": false
    }
    """

    id: str
    name: str
    iconUrl: str
    num: int
    type: int
    quality: int
    isPreview: bool


class Strategy(BaseModel):
    """攻略"""

    postId: str
    postTitle: str


class RoleCostDetail(BaseModel):
    """角色培养详情"""

    allCost: Optional[List[CultivateCost]] = None
    missingCost: Optional[List[CultivateCost]] = None
    synthetic: Optional[List[CultivateCost]] = None
    missingRoleCost: Optional[List[CultivateCost]] = None
    missingSkillCost: Optional[List[CultivateCost]] = None
    missingWeaponCost: Optional[List[CultivateCost]] = None
    roleId: int
    weaponId: int
    strategyList: Optional[List[Strategy]] = None
    showStrategy: Optional[bool] = None


class BatchRoleCostResponse(BaseModel):
    """角色培养成本"""

    roleNum: int  # 角色数量
    weaponNum: int  # 武器数量
    # preview: Dict[str, Optional[List[CultivateCost]]]
    costList: List[RoleCostDetail]  # 每个角色的详细花费
