import pytest
from qtpy import PYSIDE2, PYSIDE6


@pytest.mark.skipif(not (PYSIDE2 or PYSIDE6), reason="Only available by default in PySide")
def test_qtcharts():
    """Test the qtpy.QtCharts namespace"""
    from qtpy import QtCharts
    assert QtCharts.QtCharts.QChart is not None
