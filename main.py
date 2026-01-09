def add(a, b):
    if a < 0 or b < 0:
        print("Hello World")  # ย่อหน้า 1 ระดับ
        return 0              # ย่อหน้า 1 ระดับ (เพื่อให้ทำงานเมื่อ if เป็นจริง)
    return a + b              # ไม่ต้องย่อหน้า (เพื่อให้ทำงานเมื่อ if เป็นเท็จ)

print(add(2, 3))