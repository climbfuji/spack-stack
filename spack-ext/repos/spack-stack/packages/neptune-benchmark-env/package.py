# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys

from spack.package import *


class NeptuneBenchmarkEnv(BundlePackage):
    """Minimal environment for NEPTUNE TI-25 Benchmark"""

    # Fake URL
    homepage = "https://github.com/notavalidaccount/neptune"
    git = "https://github.com/notavalidaccount/neptune.git"

    maintainers("climbfuji", "areinecke")

    version("1.5.0")

    conflicts("platform=darwin", msg="Only supported on 'linux' and 'cray'")
    conflicts("platform=windows", msg="Only supported on 'linux' and 'cray'")

    # Basic utilities
    depends_on("cmake", type="run")
    depends_on("git", type="run")
    depends_on("wget", type="run")
    depends_on("curl", type="run")

    # I/O
    depends_on("zlib-api", type="run")
    depends_on("hdf5", type="run")
    depends_on("netcdf-c", type="run")
    depends_on("netcdf-fortran", type="run")
    depends_on("parallel-netcdf", type="run")
    #depends_on("parallelio", type="run")
    #depends_on("nccmp", type="run")

    depends_on("blas", type="run")
    depends_on("lapack", type="run")
    depends_on("numactl", type="run")

    depends_on("libyaml", type="run")
    depends_on("p4est", type="run")
    depends_on("w3emc", type="run")
    depends_on("w3nco", type="run")
    depends_on("ip@5:", type="run")
    depends_on("esmf", type="run")
    #depends_on("nco", type="run")
    depends_on("mct", type="run")

    # There is no need for install() since there is no code.
