[app]
title = Snake game
package.name = abz
package.domain = com.myinitials.myapp
source.dir = .

source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy
version = 0.1
android.permissions = INTERNET
orientation = portrait

[buildozer]
log_level = 2
android.api = 27
android.sdk = 27
android.ndk = 19b
android.ndk_api = 21
android.minapi = 21
android.allow_resizable = False
android.theme = '@android:style/Theme.NoTitleBar'
android.add_src = src/main/jni
android.black_overlay = False
android.entrypoint = org.renpy.android.PythonActivity
android.apptheme = AppTheme
android.app_color = #2196F3
android.icon_color = #2196F3
android.description = Your app description
android.author_email = your@email.com
android.author_website = http://example.com
