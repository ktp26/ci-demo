from fees import overdue_fine, summarize


def test_คืนตรงเวลาต้องไม่มีค่าปรับ():
    assert overdue_fine(0) == 0
    assert overdue_fine(-3) == 0


def test_ค่าปรับต้องไม่เกินเพดาน():
    assert overdue_fine(3) == 15
    assert overdue_fine(90) == 100


def test_ยอดรวมของหลายรายการ():
    records = [{"days_late": 2}, {"days_late": 0}, {"days_late": 40}]
    assert summarize(records) == 110
