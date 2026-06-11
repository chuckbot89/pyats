def is_supported_version(version):
    major_version = int(version.split(".")[0])
    return major_version >= 15
    
# print(is_supported_version("14.2"))