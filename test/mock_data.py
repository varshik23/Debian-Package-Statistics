"""
Mock data for testing
"""
INPUT_DATA = b"""
bin/abpoa                                               science/abpoa
bin/abpoa.avx                                           science/abpoa
bin/abpoa.avx2                                          science/abpoa
bin/abpoa.generic                                       science/abpoa
bin/abpoa.sse3                                          science/abpoa
bin/abpoa.sse4.1                                        science/abpoa
bin/abpoa.ssse3                                         science/abpoa
bin/bash                                                shells/bash
bin/bash-static                                         shells/bash-static
bin/brltty                                              admin/brltty
bin/bsd-csh                                             shells/csh
bin/btrfs                                               admin/btrfs-progs
bin/btrfs-convert                                       admin/btrfs-progs
bin/btrfs-find-root                                     admin/btrfs-progs
bin/btrfs-image                                         admin/btrfs-progs
bin/btrfs-map-logical                                   admin/btrfs-progs
bin/btrfs-select-super                                  admin/btrfs-progs
bin/btrfsck                                             admin/btrfs-progs
bin/btrfstune                                           admin/btrfs-progs
bin/bunzip2                                             utils/bzip2,utils/bzip2-mt,utils/bzip2-static
""" # Input data for the test

# List of architectures
ARC = ["all", "amd64", "arm64", "armel", "armhf", "i386", "mips64el", "mipsel", "ppc64el", "s390x"]
