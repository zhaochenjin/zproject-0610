# Git & GitHub

## Git

#### Intro
- `VCS` Version Control System
- `VSS` / `CVS` / `SVN` / `Git`
- [Git](https://git-scm.com/)
- Distributed
- Master-Branch

#### Install
- [Git 64](https://github.com/git-for-windows/git/releases/download/v2.22.0.windows.1/Git-2.22.0-64-bit.exe)

#### Git + Jetbrains
- `File | Settings | Version Control | Git | Test`

## GitHub

#### Intro
- April,2008 / Ruby on Rails / Erlang
- Git
- Open source
- 2018 M$ / 7.5B / free private repo: 3 collaborators
- Star / Fork / Follow
- Gist

#### Sign up
- username

#### GitHub + Jetbrains
- `File | Settings | Version Control
- Add GitHub User
- `C:\Users\Administrator\.gitconfig`

    ```
    [user]
        name = thu
        email = mingfei.net@gmail.com
    ```

- `.gitignore`
    ```
    .idea

    *.iml
    ```
- `READMD.md`    

- VCS | Import into Version Control | Share Project on GitHub

- GitHub | Settings | Collaborators | Add Collaborator

## Version Control

#### Reset
- `git log [--pretty=oneline]`      自加：git log 显示基本信息
- `q`
- `HEAD`
- `commit id` `SHA1`
- `git reset --hard <commit id>`    自加：git reset --hard + commit前四位数字 返回那一次
- `git reflog`       自加：显示
- `git push -f -u origin master`   自加： 如果更新到GitHub上就 git reflog 这样GitHub也改变
- `git status`

    ```
    On branch master
    Your branch is up to date with 'origin/master'.
    
    nothing to commit, working tree clean
    ```
#### Clone

#### Branch
- Create branch `Status bar | new branch`
- Working on new branch and commit & push
- Create pull request
- Code review
- Merge new branch
- Delete new branch

#### todo
- [ ] 分组
- [ ] 组长创建项目 machine-learning-project
- [ ] 组长添加组员，组员确认
- [ ] 组员检出项目
- [ ] GitHub 流程练习
- [ ] 组长提交文档

```
1. 组长：Tom: GitHub 用户名
2. 组员：
3. 项目地址：
```
