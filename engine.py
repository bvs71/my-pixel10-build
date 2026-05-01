import os
import sys

ROOT = sys.argv[1]

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

def patch_carrier():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<carrier_config_list>
  <carrier_config>
    <mcc>250</mcc>

    <bool name="carrier_volte_available_bool">true</bool>
    <bool name="carrier_wfc_ims_available_bool">true</bool>
    <bool name="enhanced_4g_lte_on_by_default_bool">true</bool>

    <int name="carrier_default_wfc_ims_mode_int">2</int>
  </carrier_config>
</carrier_config_list>
"""
    write_file(f"{ROOT}/system/etc/CarrierSettings/ims_ru.xml", xml)

def patch_permissions():
    xml = """<exceptions>
  <exception package="com.android.phone">
    <permission name="android.permission.MODIFY_PHONE_STATE" fixed="true"/>
  </exception>
  <exception package="com.android.ims">
    <permission name="android.permission.READ_PHONE_STATE" fixed="true"/>
  </exception>
</exceptions>
"""
    write_file(f"{ROOT}/system/etc/default-permissions/ims.xml", xml)

def patch_props():
    for p in ["system/build.prop", "vendor/build.prop"]:
        path = f"{ROOT}/{p}"
        if os.path.exists(path):
            with open(path, "a") as f:
                f.write("\npersist.dbg.volte_avail_ovr=1\n")
                f.write("persist.dbg.wfc_avail_ovr=1\n")
                f.write("persist.data.iwlan.enable=true\n")

def main():
    print("📡 Starting ROM patch engine...")
    patch_carrier()
    patch_permissions()
    patch_props()
    print("✅ PATCH COMPLETE")

if __name__ == "__main__":
    main()
