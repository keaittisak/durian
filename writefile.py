# การบันทึกข้อมูลลงไปเป็นไฟล์ text

from datetime import datetime


def writetext(quantity, total):
    stamp = datetime.now()
    stamp = stamp.replace(year=stamp.year+543)  # เเปลง ค.ศ. ให้เป็น พ.ศ.
    stamp = stamp.strftime('%Y-%m-%d  %H::%M::%S')

    filename = 'data.txt'  # บันทึกข้อมูลลงใน txt
    # ถ้าจะให้แสดงภาษาไทยให้ใส่ encoding ='utf-8'
    with open(filename, "a", encoding='utf-8') as file:
        file.write(
            '\n'+'วัน,เวลา : {} ทุเรียน: {} กก. รวมยอดทั้งหมด {:,.2f} บาท'.format(stamp, quantity, total))


# writetext(90, 9000)
# writetext(91, 9000)
# writetext(92, 9000)
# writetext(93, 9000)
