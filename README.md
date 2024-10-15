# sync

## DISCLAIMER (免责声明)

This software is **specifically and only** designed for users in the mainland of China. That means:

- Users in the other countries & territories may experience issues which nevertheless **will NOT be handled by me**.
- There will be **ONLY** Simplified Chinese version and **no more localization provided**.

However, since v1.3 this software is more customizable and supports different configurations. As mentioned below, you can set NTP servers, auto-exit after a run, etc.

Also, forks & PRs are welcomed.

---

本软件**专门为中国大陆用户设计和开发**。这意味着：

- 其他国家和地区的用户可能会遇到问题，但它们**将不会被我处理**。
- 只提供简体中文版本，**不提供其他本地化版本**。

不过，自 v1.3 版起，该软件的可定制性更强，支持不同的配置。如下所述，您可以设置 NTP 服务器、运行后自动退出等。

依旧欢迎 Forks 和 Pull Requests。

## 制作目的

最初做这个程序是为学校机房久未更新又拥有诸多限制的电脑校时；相当一部分设计是为了和它们兼容的。

## 以其他方式解决相同或相似的问题

如果使用的环境没有那么苛刻，您可以在不使用本程序的同时解决电脑的校时问题。

- 如果您的电脑只是需要一个自动校时：开启电脑的自动校时服务。它位于「控制面板 - 更改日期和时间 - Internet 时间 - 更改设置」。(差不多吧)
- 如果您的电脑只是会在开机以后自动回到某一个时间点 (如 2013 年 01 月 01 日 00:00)：可能只是它的时间电池没电了。您可以拆开机箱换一块。
- 如果您只是不想换 / 换不了时间电池，您可以选择打开您的注册表 (Win+R, regedit, Enter)，然后找到注册表项目 `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Config`，然后将 `MaxPosPhaseCorrection` 和 `MaxNegPhaseCorrection` 值均修改为 `0xFFFFFFF`。参考 [微软的这篇文档](https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/configure-w32ime-against-huge-time-offset)、[微软这篇文档的垃圾翻译版本](https://learn.microsoft.com/zh-cn/troubleshoot/windows-server/identity/configure-w32ime-against-huge-time-offset) 和 [这篇文章](https://www.getce.cn/show/165.html)。

## 使用方法

选中本程序后右键，点击「以管理员权限运行」，如有弹出新的窗口则点击「是」。

如果不想每次都选权限，可以在选中本程序后右键，点击「属性」，点击「兼容性」，点击「更改所有用户的设置」，勾选「以管理员身份运行此程序」，确定。

### 自启动

请自行搜索并设置计划任务程序。

或者，在 Windows 7 上，有一种简便设置方法：

1. 打开开始菜单，点击「所有程序」，右键「启动」，点击「属性」，点击「打开文件所在的位置」，进入「启动」文件夹。
2. 选中本程序，右键按住拖入「启动」文件夹中，选择「在此处创建快捷方式」。
3. 选中该快捷方式，右键，点击「属性」，点击「高级」，勾选「用管理员身份运行」，确定。
4. (可选) 退出「高级」页面后，在该属性页面设置运行方式为「最小化」。

### 配置文件

配置文件 `sync.json` 使用 JSON 语言，支持的键值对如下：

- `abort`：布尔值，控制程序在「预置列表内的所有 NTP 服务器均无响应」时应当如何处理。为 `true` 时，程序会自动终止；为 `false` 时，程序会提示用户输入日期与时间信息。默认值为 `false`。
- `autoexit`：布尔值，指定程序是否在执行完成后自动关闭窗口。为 `true` 时，程序窗口会自动关闭；为 `false` 时，程序窗口会留存，以便用户查看信息。默认值为 `true`。
- `servers`：列表，指定程序使用的 NTP 服务器。修改此项会覆盖默认值。默认值为 `['time.windows.com','cn.ntp.org.cn','cn.pool.ntp.org','ntp.aliyun.com','ntp.ntsc.ac.cn']`。

读取配置文件时，程序会自动检查每个键及其对应值的类型是否合法。如果非法，程序将跳过该键值对并显示一条警告。

`servers` 键是个例外，程序只会检查它的对应值是否是一个列表，但不会检查列表中的内容。如果列表中的某 (些) 元素并非合法的 NTP 服务器，程序将会在调用对应元素时显示「未响应」警告。

## 兼容性

- 使用 pyinstaller 在 Windows 7 (32 bit) 环境下打包。理论上应该能兼容它和它以上的所有 Windows 版本，但未经全面测试。
- 不对 Windows 7 以下版本的系统进行特别兼容设计，换句话说能用用不能用也不管。
- 仅 Windows，不对其他平台兼容。
- 需要拥有管理员权限。

## 已知问题

- 部分甚至相当一部分杀毒软件会将本软件误报为病毒，如误报为 Trojan 木马。**本软件不含木马病毒代码**并已全部开源，可自行下载整库后运行 toolbox 内的 `pack.bat` 进行打包构建 (需要拥有 Python 环境、ntplib 第三方库和 pyinstaller 第三方库)。我也会向 360 反馈误报，以在机房正常使用。
