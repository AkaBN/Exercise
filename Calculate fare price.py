distance = int(input())
fare = 0.0

    # คำนวณค่าบริการสำหรับ 1 กิโลเมตรแรก
if distance >= 0 and distance <=1:
    fare +=35.00

    # คำนวณค่าบริการสำหรับระยะทางเกินกว่า 1 กิโลเมตรถึงกิโลเมตรที่ 10
elif distance >1 and distance <= 10:
    fare += distance * 5.50

    # คำนวณค่าบริการสำหรับระยะทางเกินกว่า 10 กิโลเมตรถึงกิโลเมตรที่ 20
elif distance > 10 and distance <=20:
    fare += distance * 6.50

    # คำนวณค่าบริการสำหรับระยะทางเกินกว่า 20 กิโลเมตรถึงกิโลเมตรที่ 40
elif distance > 20 and distance <=40:
    fare += distance * 7.50

    # คำนวณค่าบริการสำหรับระยะทางเกินกว่า 40 กิโลเมตรถึงกิโลเมตรที่ 60
elif distance > 40 and distance <=60:
    fare += distance * 8.00

    # คำนวณค่าบริการสำหรับระยะทางเกินกว่า 60 กิโลเมตรถึงกิโลเมตรที่ 80
elif distance > 60 and distance <=80:
    fare += distance * 9.00

    # คำนวณค่าบริการสำหรับระยะทางเกินกว่า 80 กิโลเมตรขึ้นไป
elif distance > 80 :
    fare += distance * 10.50

print(fare+0.0)

