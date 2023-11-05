# sync

## DISCLAIMER (免责声明)

This software is **specifically and only** designed for users in the mainland of China. That means:

- Users in the other countries & territories may experience issues which nevertheless **will NOT be handled by me**.
- There will be **ONLY** Simplified Chinese version and **no more localization provided**.

Despite this, forks & PRs are still welcomed.

---

本软件**专门为中国大陆用户设计和开发**。这意味着：

- 其他国家和地区的用户可能会遇到问题，但它们**将不会被我处理**。
- 只提供简体中文版本，**不提供其他本地化版本**。

尽管如此，依旧欢迎 Forks 和 Pull Requests。

## 制作目的

最初做这个程序是为学校机房久未更新又拥有诸多限制的电脑校时；相当一部分设计是为了和它们兼容的。

## 以其他方式解决相同或相似的问题

如果使用的环境没有那么苛刻，您可以在不使用本程序的同时解决电脑的校时问题。

-如果您的电脑只是需要一个自动校时：开启电脑的自动校时服务。它位于「控制面板-更改日期和时间-Internet 时间-更改设置」 (差不多吧)
- 如果您的电脑只是会在开机以后自动回到某一个时间点 (如 2013 年 1 月 1 日 00:00)：可能只是它的时间电池没电了。您可以拆开机箱换一块。

## 使用方法

## 兼容性

- 使用 pyinstaller 在 Windows 7(32 bit) 环境下打包。理论上应该能兼容它和它以上的所有 Windows 版本，但未经全面测试。
- 不对 Windows 7 以下版本的系统进行特别兼容设计，换句话说能用用不能用也不管。
- 仅 Windows，不对其他平台兼容。
- 需要拥有管理员权限。

## 已知问题

- 部分甚至相当一部分杀毒软件会将本软件误报为病毒，如误报为 Trojan 木马。**本软件不含木马病毒代码**并已全部开源，可自行下载整库后运行 toolbox 内的 `pack.bat` 进行打包构建 (需要拥有 Python 环境、ntplib 第三方库和 pyinstaller 第三方库)。
- 如果 NTP 服务器无响应，只会提示输入日期而不会提示输入时间，反而选择拿系统时间服务校准的傻逼逻辑。
