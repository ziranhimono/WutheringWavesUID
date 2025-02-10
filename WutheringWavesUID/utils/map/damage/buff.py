from ....utils.damage.abstract import WavesCharRegister


def shouanren_buff(attr, chain, resonLevel, isGroup):
    # 守岸人buff
    char_clz = WavesCharRegister.find_class(1505)
    if char_clz:
        s = char_clz()
        s.do_buff(attr, chain=chain, resonLevel=resonLevel, isGroup=isGroup)


def sanhua_buff(attr, chain, resonLevel, isGroup):
    # 散华buff
    char_clz = WavesCharRegister.find_class(1102)
    if char_clz:
        s = char_clz()
        s.do_buff(attr, chain=chain, resonLevel=resonLevel, isGroup=isGroup)


def motefei_buff(attr, chain, resonLevel, isGroup):
    # 莫特斐buff
    char_clz = WavesCharRegister.find_class(1204)
    if char_clz:
        s = char_clz()
        s.do_buff(attr, chain=chain, resonLevel=resonLevel, isGroup=isGroup)


def weilinai_buff(attr, chain, resonLevel, isGroup):
    # 维里奈buff
    char_clz = WavesCharRegister.find_class(1503)
    if char_clz:
        s = char_clz()
        s.do_buff(attr, chain=chain, resonLevel=resonLevel, isGroup=isGroup)


def zhezhi_buff(attr, chain, resonLevel, isGroup):
    # 折枝buff
    char_clz = WavesCharRegister.find_class(1105)
    if char_clz:
        s = char_clz()
        s.do_buff(attr, chain=chain, resonLevel=resonLevel, isGroup=isGroup)


def changli_buff(attr, chain, resonLevel, isGroup):
    # 长离buff
    char_clz = WavesCharRegister.find_class(1205)
    if char_clz:
        s = char_clz()
        s.do_buff(attr, chain=chain, resonLevel=resonLevel, isGroup=isGroup)


def dengdeng_buff(attr, chain, resonLevel, isGroup):
    # 灯灯buff
    char_clz = WavesCharRegister.find_class(1504)
    if char_clz:
        s = char_clz()
        s.do_buff(attr, chain=chain, resonLevel=resonLevel, isGroup=isGroup)


def luokeke_buff(attr, chain, resonLevel, isGroup):
    # 洛可可buff
    char_clz = WavesCharRegister.find_class(1606)
    if char_clz:
        s = char_clz()
        s.do_buff(attr, chain=chain, resonLevel=resonLevel, isGroup=isGroup)


def guangzhu_buff(attr, chain, resonLevel, isGroup):
    # 光主buff
    char_clz = WavesCharRegister.find_class(1501)
    if char_clz:
        s = char_clz()
        s.do_buff(attr, chain=chain, resonLevel=resonLevel, isGroup=isGroup)
