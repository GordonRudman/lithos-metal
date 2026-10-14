from ..base import MetalBackend


class Backend(MetalBackend):
    """Native fallback pending measurements on the 40-core M3 Max.

    Does not inherit the 30-core M3 Max profile: core count and measured lane
    order are a different device (m3_max_30c's own docstring already says so).
    Tensor acceleration and mixer fusion stay off until `tools/profile_writer.py`
    is run on this exact chip.
    """
    id = "m3_max_40c"
