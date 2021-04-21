# Babuk Vaccine
This python script blocks encryption from happening if your system is infected by the Babuk Ransomware

It does so using two methods. 

## ECDH
In the early strains, the encryption was depending on the creation of a file called `ecdh_pub_k.bin`.
Creating this file in the `%APPDATA%` folder using CreateFile and the shareMode parameter at value 0 will disable its access for other processes, and Babuk does not encryt any drives if it is not able to open this file.

![image](https://user-images.githubusercontent.com/81870557/115510538-28dcba80-a280-11eb-8eb0-43029109d423.png)

## Mutexes
For later strains, the encryption depends on the presence of a certain mutex. Its value will change with the strain. It can either be the value `babuk_v[x]` with `[x]` being replaced by the version number. We spotted version 2 and 3 in the wild. 
Another mutex encountered, and the one Babuk’s operator are using even today is `DoYouWantToHaveSexWithCuongDong` which is a taunt against one of the first researchers to have made an article about Babuk : http://chuongdong.com/reverse%20engineering/2021/01/03/BabukRansomware/
