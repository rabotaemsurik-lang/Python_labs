import os
from task4 import KmrWork, Statistic

def test_csv_read():
    kmr = KmrWork("kmr1.csv", 1)
    assert len(kmr.data) > 0

def test_avg_stat():
    kmr = KmrWork("kmr1.csv", 1)
    stat = kmr.avg_stat(kmr.data)
    assert isinstance(stat, tuple)
    assert len(stat) == len(kmr.data[0]) - 3

def test_marks_stat():
    kmr = KmrWork("kmr1.csv", 1)
    marks = kmr.marks_stat(kmr.data)
    assert isinstance(marks, dict)
    assert all(isinstance(k, int) for k in marks.keys())

def test_marks_per_time():
    kmr = KmrWork("kmr1.csv", 1)
    mpt = kmr.marks_per_time(kmr.data)
    assert isinstance(mpt, dict)
    assert len(mpt) == len(kmr.data)

def test_best_marks_per_time():
    kmr = KmrWork("kmr1.csv", 1)
    best = kmr.best_marks_per_time(kmr.data, 0, 20)
    assert isinstance(best, tuple)
    assert len(best) <= 5
