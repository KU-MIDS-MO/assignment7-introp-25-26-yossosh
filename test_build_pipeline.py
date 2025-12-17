import pytest
from build_pipeline import build_pipeline

def test_pipeline_order():
    f = build_pipeline(["double", "square"])
    assert f(3) == 36

def test_pipeline_unknown_op():
    with pytest.raises(KeyError):
        build_pipeline(["double", "explode"])

def test_pipeline_multiple_steps():
    f = build_pipeline(["triple", "double", "square"])
    assert f(2) == 144
