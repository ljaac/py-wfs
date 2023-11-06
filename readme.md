## 基本操作

```shell
# convert ui file into py file
pyuic5 -x wfs.ui -o wf_ui.py
```



```shell
# 使用pyinstaller打包成exe
pyinstaller -F --noconsole -i wfs.ico --add-data "nltk_data;nltk_data" wfs.py 
# 上面命令会产生一个Spec文件，Spec文件已经包含了各种参数，再次执行pyinstaller时，可以直接利用spec文件来打包exe
pyinstaller wfs.spec
```

