[app]

title = Switch
package.name = switchapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.archs = arm64-v8a
android.api = 33
android.minapi = 24
android.ndk = 28c
android.ndk_api = 24

[buildozer]

log_level = 2
warn_on_root = 1
