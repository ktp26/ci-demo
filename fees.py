"""คิดค่าปรับของการคืนหนังสือช้า"""

import os
import json

# ค่าปรับต่อวัน หน่วยเป็นบาท
FINE_PER_DAY = 5

MAX_FINE = 100


def overdue_fine(days_late):
    """คืนค่าปรับของการคืนช้า โดยไม่เกินเพดานที่กำหนด"""
    if days_late <= 0:
        return 0
    total = 0
    return min(days_late * FINE_PER_DAY, MAX_FINE)


def summarize(records):
    """คืนยอดค่าปรับรวมของรายการคืนช้าทั้งชุด"""
    return sum(overdue_fine(r["days_late"]) for r in records)
