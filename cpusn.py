#-*- coding:utf-8 -*-
#使用utf-8编码
import os,sys
import platform
import wmi
import psutil
import time
cpuinfo = wmi.WMI()

print("此计算机名称：{}".format(platform.node())+"\n")

print("当前操作系统及版本号：{}".format(platform.platform()),end=" ,")
print("是{}位操作系统".format(platform.architecture()[0][0:2])+"\n")

print("当前登录账户信息：{}".format(psutil.users())+"\n")
phymem=psutil.virtual_memory()
type(phymem.used)
round(phymem.used/1024/1024/1024,1)

# for s in cpuinfo.Win32_StartupCommand():
#       print("[%s] %s <%s>" % (s.Location, s.Caption, s.Command))


for interface in cpuinfo.Win32_NetworkAdapterConfiguration(IPEnabled=1):
    print("Mac:%s" % interface.MACAddress+"\n")
for ip_address in interface.IPAddress:
    print("ip_add:%s" % ip_address+"\n")


for bios_id in cpuinfo.Win32_BIOS():

   # bios_id.BiosCharacteristics   BIOS特征码
    print("BIOS版本："+bios_id.Version+"\n")                           #BIOS版本
    print("BIOS固件生产厂家:"+bios_id.Manufacturer.strip()+"\n")                 #BIOS固件生产厂家
   # tmpmsg['ReleaseDate'] = bios_id.ReleaseDate                   #BIOS释放日期
    # print("系统管理规范版本"+bios_id.SMBIOSBIOSVersion)       #系统管理规范版本


for board_id in cpuinfo.Win32_BaseBoard():
    print("主板生产厂家:"+board_id.Manufacturer+"\n")       #主板生产品牌厂家
    print("主板型号:"+board_id.Product+"\n")                #主板型号



print("您的CPU架构为:" + platform.machine()+"\n")




#   print("您的CPU家族为:" + platform.processor())

for cpu in cpuinfo.Win32_Processor():
    print("您的CPU名称为:" + cpu.Name+"\n")
#   print("您的CPU序列号为:" + cpu.ProcessorId.strip()+"\n")
    
cores = cpu.NumberOfCores

threads = psutil.cpu_count()
print("您的CPU为{}核{}线程".format(cores,threads)+"\n")

print('您的总内存:',str(round(phymem.total/1024/1024/1024,1))+'G'+"\n")
round(phymem.free/1024/1024/1024,5)
print("内存占用率 {0:.0%}".format(round(phymem.used/1024/1024/1024,1)/\
                            round(phymem.total/1024/1024/1024,1))+"\n")

for disk in cpuinfo.Win32_logicalDisk(DriveType=3):
    print("分区{}可用空间：{:.1f}%".format(disk.Caption,100*\
                                    int(disk.FreeSpace)/int(disk.Size))+"\n")










