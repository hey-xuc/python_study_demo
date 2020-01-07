from random import randint

money = 1000    # 初始资金
while money > 0:
    print('你的资金为: %d' % money)
    while True:
        bet = int(input('请下注')) # 下注金额
        # 判断下注金额是否合法
        if 0 < bet <= money:
            break
        else:
            print('下注失败')
    # 开始摇色子
    first = randint(1, 6) + randint(1, 6)
    print('摇出了 %d 点' % first)
    if first == 7 or first == 11:
        money += bet
        print('玩家胜')
        # 玩家胜
    elif first == 2 or first == 3 or first == 12:
        money -= bet
        print('庄家胜')
        # 庄家胜
    else:
        # 继续摇色子
        while True:
            two = randint(1, 6) + randint(1, 6)
            print('摇出了 %d 点' % two)
            if two == first:
                # 玩家胜
                print('玩家胜')
                money += bet
                break
            elif two == 7:
                # 庄家胜
                money -= bet
                print('庄家胜')
                break
print('你已经破产了')
    
        
    