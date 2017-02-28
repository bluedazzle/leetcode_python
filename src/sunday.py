# coding: utf-8

# author: RaPoSpectre
# time: 2016-10-31


def sunday(s, model):
    match = False
    ms = 0
    me = len(model)

    if s == model:
        print '匹配成功,位置: s[{0}]->s[{1}]'.format(0, len(model))
        return True

    while 1:
        p = s[ms: me]
        if model == p:
            match = True
            print '匹配成功,位置: s[{0}]->s[{1}]'.format(ms, me)
            break
        if me >= len(s):
            break
        sign = s[me]
        if sign in model:
            posi = model.rfind(sign)
            offset = len(model) - posi
            ms += offset
            me += offset
        else:
            ms += len(model)
            me += len(model)
    return match


# print sunday('123', '4')