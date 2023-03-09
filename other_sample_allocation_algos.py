# Problem: Same priority customers division of power not correct

# slots=['C1/C2','C4','C5']
# allWindmills=dfWindmills['Windmill'].tolist()
# allCustomers=dfConsumption['Customer'].tolist()
# generationTable.to_excel('generationTable.xlsx')
# consumptionTable.to_excel('consumptionTable.xlsx')


# for currWindmill in allWindmills:

#     for slot in slots:

#         currSlotGen=generationTable.loc[generationTable['Windmill']==currWindmill,slot].values[0]
#         # print(currSlotGen)
#         columnToCheck=slot+" Priority/"+currWindmill
#         dfSortedCustomer=dfx.sort_values(by=columnToCheck).copy()

#         dfSortedCustomer=dfSortedCustomer[dfSortedCustomer[columnToCheck]>0]

#         # dfSortedCustomer.to_excel('dfSortedCustomer.xlsx')

#         allCustomers=dfSortedCustomer.sort_values(by=columnToCheck)['Customer'].tolist()
#         # print(dfSortedCustomer['C1/C2 Priority/735'])# all customers sorted in priority order
#         # print(dfSortedCustomer)
#         for customer in allCustomers:
#             currConsumption=consumptionTable.loc[consumptionTable['Customer']==customer,slot].values[0]
#             currPriority=dfSortedCustomer.loc[dfSortedCustomer['Customer']==customer,columnToCheck].values[0]
#             currPriorityCount=len(dfSortedCustomer[dfSortedCustomer[columnToCheck]==currPriority])
#             print(customer,currPriority,currPriorityCount)
#             if currPriorityCount==1:
#                 if currSlotGen<=0:
#                     generationTable.loc[generationTable['Windmill']==currWindmill,slot]=currSlotGen

#                     break
#                 elif currConsumption<=0:
#                     consumptionTable.loc[consumptionTable['Customer']==customer,slot]=currConsumption
#                     continue
#                 elif currSlotGen>currConsumption:
#                     allocationTable['Windmill'].append(currWindmill)
#                     allocationTable['Customer'].append(customer)
#                     allocationTable[slot].append(currConsumption)
#                     for x in slots:
#                         if x!=slot:
#                             allocationTable[x].append(0)
#                     currSlotGen=currSlotGen-currConsumption
#                     currConsumption=0
#                     generationTable.loc[generationTable['Windmill']==currWindmill,slot]=currSlotGen
#                     consumptionTable.loc[consumptionTable['Customer']==customer,slot]=currConsumption

#                 elif currConsumption>=currSlotGen:
#                     allocationTable['Windmill'].append(currWindmill)
#                     allocationTable['Customer'].append(customer)
#                     allocationTable[slot].append(currSlotGen)
#                     for x in slots:
#                         if x!=slot:
#                             allocationTable[x].append(0)
#                     currConsumption=currConsumption-currSlotGen
#                     currSlotGen=0
#                     generationTable.loc[generationTable['Windmill']==currWindmill,slot]=currSlotGen
#                     consumptionTable.loc[consumptionTable['Customer']==customer,slot]=currConsumption
#             else:
#                 # problem: Its currently only taking the first customer in the priority list and splitting by total customers, but rest of the customers are pending

#                 if currSlotGen<=0:
#                     generationTable.loc[generationTable['Windmill']==currWindmill,slot]=currSlotGen
#                     break
#                 elif currConsumption<=0:
#                     consumptionTable.loc[consumptionTable['Customer']==customer,slot]=currConsumption
#                     continue
#                 elif (currSlotGen/currPriorityCount)>currConsumption:

#                     allocationTable['Windmill'].append(currWindmill)
#                     allocationTable['Customer'].append(customer)
#                     allocationTable[slot].append(currConsumption)
#                     for x in slots:
#                         if x!=slot:
#                             allocationTable[x].append(0)
#                     currSlotGen=currSlotGen-currConsumption/currPriorityCount
#                     currConsumption=0
#                     generationTable.loc[generationTable['Windmill']==currWindmill,slot]=currSlotGen
#                     consumptionTable.loc[consumptionTable['Customer']==customer,slot]=currConsumption

#                 elif currConsumption>=(currSlotGen/currPriorityCount):
#                     allocationTable['Windmill'].append(currWindmill)
#                     allocationTable['Customer'].append(customer)
#                     allocationTable[slot].append(currSlotGen/currPriorityCount)
#                     for x in slots:
#                         if x!=slot:
#                             allocationTable[x].append(0)
#                     currConsumption=currConsumption-currSlotGen/currPriorityCount
#                     currSlotGen=0
#                     generationTable.loc[generationTable['Windmill']==currWindmill,slot]=currSlotGen
#                     consumptionTable.loc[consumptionTable['Customer']==customer,slot]=currConsumption
#         # print("-------------------------")
# # print(len(allocationTable['Windmill']),len(allocationTable['Customer']),len(allocationTable['C1/C2']),len(allocationTable['C4']),len(allocationTable['C5']))
# # print(allocationTable)
# dfAllocation=pd.DataFrame(allocationTable)
# dfAllocation.to_excel('dfAllocation.xlsx')


# generationTable.to_excel('generationTable.xlsx')
# consumptionTable.to_excel('consumptionTable.xlsx')


# slots=['C1/C2','C4','C5']
# for index,currWindmill in generationTable.iterrows():
#     # print(currWindmill['Windmill'])
#     # print(currWindmill['C1/C2'])
#     # print(currWindmill['C4'])
#     # print(currWindmill['C5'])
#     # print(customerMask.index) # this index contains the indexes of df where customers are valid for this windmill
#     customerMask=df[str(currWindmill['Windmill'])]

#     customerIndex=customerMask[customerMask>0]
#     customerList=df.loc[customerIndex.index]
#     customerList.sort_values(by=str(currWindmill['Windmill']),inplace=True)
#     maxPriority=customerList[str(currWindmill['Windmill'])].max()
#     # customerList=customerList['Customer'].to_list()
#     customerDict={'Customer':[x for x in customerList["Customer"]],'Priority':[x for x in customerList[str(currWindmill['Windmill'])]]}
#     # print(customerList[str(currWindmill['Windmill'])].value_counts()[priority]) # this gives us the count of each priority
#     # if priorty 1 is multiple times then split the generation equally
#     for currIndex in range(len(customerDict['Customer'])):
#         if customerList[str(currWindmill['Windmill'])].value_counts()[customerDict['Priority'][currIndex]]==1:
#             allocationTable['Customer'].append(customerDict['Customer'][currIndex])
#             allocationTable['Windmill'].append(currWindmill['Windmill'])
#             # FOR C1 C2 SLOTs
#             consumptionC1C2=consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C1/C2"].values[0]
#             availableC1C2=currWindmill['C1/C2']
#             if availableC1C2>=consumptionC1C2 and availableC1C2>0 and consumptionC1C2>0:
#                 allocationTable['C1/C2'].append(consumptionC1C2)
#                 currWindmill['C1/C2']-=consumptionC1C2
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C1/C2"]=0
#             elif availableC1C2>0 and availableC1C2<consumptionC1C2 and consumptionC1C2>0:

#                 allocationTable['C1/C2'].append(availableC1C2)

#                 currWindmill['C1/C2']-=availableC1C2
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C1/C2"]-=availableC1C2
#             else:
#                 allocationTable['C1/C2'].append(0)
#             # FOR C4 SLOT
#             consumptionC4=consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C4"].values[0]
#             availableC4=currWindmill['C4']
#             if availableC4>=consumptionC4 and availableC4>0 and consumptionC4>0:


#                 allocationTable['C4'].append(consumptionC4)

#                 currWindmill['C4']-=consumptionC4
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C4"]=0
#             elif availableC4>0 and availableC4<consumptionC4 and consumptionC4>0:


#                 allocationTable['C4'].append(availableC4)

#                 currWindmill['C4']-=availableC4
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C4"]-=availableC4
#             else:
#                 allocationTable['C4'].append(0)
#             # FOR C5 SLOT
#             consumptionC5=consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C5"].values[0]
#             availableC5=currWindmill['C5']
#             if availableC5>=consumptionC5 and availableC5>0 and consumptionC5>0:
#                 allocationTable['C5'].append(consumptionC5)
#                 currWindmill['C5']-=consumptionC5
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C5"]=0
#             elif availableC5>0 and availableC5<consumptionC5 and consumptionC5>0:
#                 allocationTable['C5'].append(availableC5)
#                 currWindmill['C5']-=availableC5
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C5"]-=availableC5
#             else:
#                 allocationTable['C5'].append(0)

#         # else split the generation equally between the customers with same priority
#         elif customerList[str(currWindmill['Windmill'])].value_counts()[customerDict['Priority'][currIndex]]>1:
#             allocationTable['Customer'].append(customerDict['Customer'][currIndex])
#             allocationTable['Windmill'].append(currWindmill['Windmill'])
#             # for C1 C2 slots
#             availableC1C2=currWindmill['C1/C2']/customerList[str(currWindmill['Windmill'])].value_counts()[customerDict['Priority'][currIndex]]
#             consumptionC1C2=consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C1/C2"].values[0]
#             if availableC1C2>=consumptionC1C2 and availableC1C2>0 and consumptionC1C2>0:
#                 allocationTable['C1/C2'].append(consumptionC1C2)
#                 currWindmill['C1/C2']-=consumptionC1C2
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C1/C2"]=0
#             elif availableC1C2>0 and availableC1C2<consumptionC1C2 and consumptionC1C2>0:
#                 allocationTable['C1/C2'].append(availableC1C2)
#                 currWindmill['C1/C2']-=availableC1C2
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C1/C2"]-=availableC1C2
#             else:
#                 allocationTable['C1/C2'].append(0)
#             # for C4 slot
#             availableC4=currWindmill['C4']/customerList[str(currWindmill['Windmill'])].value_counts()[customerDict['Priority'][currIndex]]
#             consumptionC4=consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C4"].values[0]
#             if availableC4>=consumptionC4 and availableC4>0 and consumptionC4>0:
#                 allocationTable['C4'].append(consumptionC4)

#                 currWindmill['C4']-=consumptionC4
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C4"]=0
#             elif availableC4>0 and availableC4<consumptionC4 and consumptionC4>0:
#                 allocationTable['C4'].append(availableC4)

#                 currWindmill['C4']-=availableC4
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C4"]-=availableC4
#             else:
#                 allocationTable['C4'].append(0)
#             # for C5 slot
#             availableC5=currWindmill['C5']/customerList[str(currWindmill['Windmill'])].value_counts()[customerDict['Priority'][currIndex]]
#             consumptionC5=consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C5"].values[0]
#             if availableC5>=consumptionC5 and availableC5>0 and consumptionC5>0:
#                 allocationTable['C5'].append(consumptionC5)
#                 currWindmill['C5']-=consumptionC5
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C5"]=0
#             elif availableC5>0 and availableC5<consumptionC5 and consumptionC5>0:
#                 allocationTable['C5'].append(availableC5)
#                 currWindmill['C5']-=availableC5
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C5"]-=availableC5
#             else:
#                 allocationTable['C5'].append(0)
#         print(generationTable,consumptionTable)


# print(allocationTable)
# print(len(allocationTable['Customer']),len(allocationTable['Windmill']),len(allocationTable['C1/C2']),len(allocationTable['C4']),len(allocationTable['C5']))
# pd.DataFrame(allocationTable).to_csv("allocationTable.csv",index=False)


# for currIndex in range(len(customerDict['Customer'])):
#         if customerList[str(currWindmill['Windmill'])].value_counts()[customerDict['Priority'][currIndex]]==1:
#             allocationTable['Customer'].append(customerDict['Customer'][currIndex])
#             allocationTable['Windmill'].append(currWindmill['Windmill'])
#             # FOR C1 C2 SLOTs
#             consumptionC1C2=consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C1/C2"].values[0]
#             availableC1C2=currWindmill['C1/C2']
#             if availableC1C2>=consumptionC1C2 and availableC1C2>0 and consumptionC1C2>0:
#                 allocationTable['C1/C2'].append(consumptionC1C2)
#                 currWindmill['C1/C2']-=consumptionC1C2
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C1/C2"]=0
#             elif availableC1C2>0 and availableC1C2<consumptionC1C2 and consumptionC1C2>0:

#                 allocationTable['C1/C2'].append(availableC1C2)

#                 currWindmill['C1/C2']-=availableC1C2
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C1/C2"]-=availableC1C2
#             # FOR C4 SLOT
#             consumptionC4=consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C4"].values[0]
#             availableC4=currWindmill['C4']
#             if availableC4>=consumptionC4 and availableC4>0 and consumptionC4>0:


#                 allocationTable['C4'].append(consumptionC4)

#                 currWindmill['C4']-=consumptionC4
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C4"]=0
#             elif availableC4>0 and availableC4<consumptionC4 and consumptionC4>0:


#                 allocationTable['C4'].append(availableC4)

#                 currWindmill['C4']-=availableC4
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C4"]-=availableC4
#             # FOR C5 SLOT
#             consumptionC5=consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C5"].values[0]
#             availableC5=currWindmill['C5']
#             if availableC5>=consumptionC5 and availableC5>0 and consumptionC5>0:
#                 allocationTable['C5'].append(consumptionC5)
#                 currWindmill['C5']-=consumptionC5
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C5"]=0
#             elif availableC5>0 and availableC5<consumptionC5 and consumptionC5>0:
#                 allocationTable['C5'].append(availableC5)
#                 currWindmill['C5']-=availableC5
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C5"]-=availableC5


#         # else split the generation equally between the customers with same priority
#         else:
#             allocationTable['Customer'].append(customerDict['Customer'][currIndex])
#             allocationTable['Windmill'].append(currWindmill['Windmill'])
#             # for C1 C2 slots
#             availableC1C2=currWindmill['C1/C2']/customerList[str(currWindmill['Windmill'])].value_counts()[customerDict['Priority'][currIndex]]
#             consumptionC1C2=consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C1/C2"].values[0]
#             if availableC1C2>=consumptionC1C2 and availableC1C2>0 and consumptionC1C2>0:
#                 allocationTable['C1/C2'].append(consumptionC1C2)
#                 currWindmill['C1/C2']-=consumptionC1C2
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C1/C2"]=0
#             elif availableC1C2>0 and availableC1C2<consumptionC1C2 and consumptionC1C2>0:
#                 allocationTable['C1/C2'].append(availableC1C2)
#                 currWindmill['C1/C2']-=availableC1C2
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C1/C2"]-=availableC1C2
#             # for C4 slot
#             availableC4=currWindmill['C4']/customerList[str(currWindmill['Windmill'])].value_counts()[customerDict['Priority'][currIndex]]
#             consumptionC4=consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C4"].values[0]
#             if availableC4>=consumptionC4 and availableC4>0 and consumptionC4>0:
#                 allocationTable['C4'].append(consumptionC4)

#                 currWindmill['C4']-=consumptionC4
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C4"]=0
#             elif availableC4>0 and availableC4<consumptionC4 and consumptionC4>0:
#                 allocationTable['C4'].append(availableC4)

#                 currWindmill['C4']-=availableC4
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C4"]-=availableC4
#             # for C5 slot
#             availableC5=currWindmill['C5']/customerList[str(currWindmill['Windmill'])].value_counts()[customerDict['Priority'][currIndex]]
#             consumptionC5=consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C5"].values[0]
#             if availableC5>=consumptionC5 and availableC5>0 and consumptionC5>0:
#                 allocationTable['C5'].append(consumptionC5)
#                 currWindmill['C5']-=consumptionC5
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C5"]=0
#             elif availableC5>0 and availableC5<consumptionC5 and consumptionC5>0:
#                 allocationTable['C5'].append(availableC5)
#                 currWindmill['C5']-=availableC5
#                 consumptionTable.loc[consumptionTable["Customer"]==customerDict['Customer'][currIndex],"C5"]-=availableC5
