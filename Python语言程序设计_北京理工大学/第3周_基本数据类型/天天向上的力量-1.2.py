#===========================================#
#                                           #
# ==============工作日的力量=================#
#　　　　　　　　　　　　　　　　　　　　　　   #　
#                                           #
# === 一年365天，一周5个工作日，每天进步1% === #
#                                           #
# ==== 一年365天，一周2个休息日，每天退步1% ===#
#                                           #
#  ======== 这种工作日的力量，如何呢? ======= #
#                                           #
#===========================================#


dayup = 1.0
dayfactor = 0.01
for i in range (365):
    if i % 7 in [ 6 , 0 ]:
        dayup = dayup * ( 1 - dayfactor )
    else:
        dayup = dayup * ( 1 + dayfactor )
    print (" 工作日的力量：{:.2f} " .format ( dayup ))

