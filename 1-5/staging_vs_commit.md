# Staging 과 Commit의 차이: 도시락에 비유하기

## Git 상에서 Staging을 할 때: 도시락에 넣은 반찬을 고르는 단계
    - staging: git add  커맨드를 활용함
    - commit 할 파일을 미리 준비해두는 것.
    - "이 변경사항을 다음 커밋에 포함할 것이다"라고 표시하는 단계.
    - 이 상태는 기록에는 남지 않는다.
    - 왜 생겼는가: SVN 같은 VCS는 작업 중인 "모든" 변경이 통째로 Commit되어서 불편했음.
    - 그래서 Git은: Commit을 하기 전에 Staging을 중간에 두어서 Commit에 어떤 변경을 포함할 지 내가 고를 수 있게 함.

## Git 상에서 Commit을 할 때: 도시락 포장 완료 선언. 냉장고에 저장
    - local 저장소 (내 컴퓨터의 .git)에 변경 기록 (snapshot)이 확정됨
    - git log에 남고, 고유한 commit hash가 생성됨.
    - 왜 생겼는가: Snapshot의 보존 및 이력 관리를 위해서 생김. (이것이 Git의 핵심)
    - Commit이 Git의 history log이고, log, revert, branch등이 모두 Commit 단위로 작동함. (여기서부터는 기록된다!)


## Push: Github에 올리기: 도시락 GitHub으로 배달!
    - Push는 Local에 이미 commit된 기록을 GitHub 등의 원격 저장소로 upload하는 단계
    - GitHub에 올라가도 Commit 시간은 원래 commit했던 시점으로 기록됨.
    - 생긴 이유: Git은 이제 Distributed VCS이다. 말인즉슨 네트워크가 끊긴 환경에서도 Commit은 로컬에서 자유롭게 하고, 나중에 네트워크가 연결될 때 한번에 Push로 동기화할 수 있게 만들어둔 것이다. ("분산된" 버전 관리 시스템의 존재이유, 주요 기능)

이렇게 3단계로 구분되었기 때문에 자유도와 안정성이 보장된다고 볼 수 있다.
    - 원할 떄 기록
    - 네트워크에 없어도 단독작업 가능
    - 잘못된 기록은 revert도 쉬움
