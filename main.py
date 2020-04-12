x,y=map(int,input().split())
dp=[]
for i in range(0,y):
    dp.append([])
    for j in range(0,x):
        dp[i].append(0)
pull = [[0,0]]
pull2=[]
dp[0][0]=1
maxX, maxY =0,0
run=0
while run<2:
    for i in pull:
        try:
            dp[i[0]+1][i[1]+2]+=dp[i[0]][i[1]]
            if ([i[0]+1,i[1]+2] in pull2)==False:
                pull2.append([i[0]+1,i[1]+2])
        except IndexError:
            run+=1
        try:
            dp[i[0]+2][i[1]+1]+=dp[i[0]][i[1]]
            if ([i[0]+2,i[1]+1] in pull2)==False:
                pull2.append([i[0]+2,i[1]+1])
        except IndexError:
            run+=1
    maxX+=1
    maxY+=1
    pull = pull2
    pull2=[]
print('Ответ:'+str(dp[y-1][x-1]))
