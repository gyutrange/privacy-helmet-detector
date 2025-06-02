# 🛠️ Helmet & Privacy Monitoring System

AI 기반의 산업 현장용 실시간 안전 감시 시스템입니다. 본 프로젝트는 작업자의 **안전모 착용 여부**를 판단하고, **얼굴을 마스킹**하여 프라이버시를 보호함으로써 산업재해를 줄이고 개인정보를 보호하는 것을 목표로 합니다.

---

## 🎯 프로젝트 목표

산업 현장의 **안전성과 프라이버시를 동시에 강화**하는 **AI 기반 실시간 모니터링 시스템**을 구축하고자 합니다.

---

## 🔍 배경 및 문제 인식

- **산업재해의 지속적 발생**  
  고용노동부 통계에 따르면 산업현장 내 재해가 꾸준히 발생하고 있음.

- **업무상 질병자의 증가**  
  반복된 노출, 환경 문제 등으로 작업자 건강에 위협이 커지고 있음.

- **산업재해가 기업의 수익성과 성장에 악영향**  
  안전 문제는 단순한 복지 문제가 아닌 경영 리스크 요소로 작용.

---

## ✅ 해결 목표 및 기술적 접근

| 항목 | 기술/도구 | 설명 |
|------|------------|------|
| 얼굴 감지 | DNN, Haar Cascade | 마스킹 전처리용 얼굴 인식 |
| 실시간 마스킹 | OpenCV | 프라이버시 보호용 블러 처리 |
| 안전모 감지 | YOLOv5 | 헬멧 착용 여부 분류 |
| 데이터 | Roboflow (Hard Hat Workers) | 다양한 클래스 및 색상 포함 |

---

## 🧪 예상 효과

- ✅ 작업자 **프라이버시 침해 최소화** → GDPR 등 준수
- ✅ **안전모 착용 여부 실시간 탐지** → 산업재해 예방
- ✅ **익명화된 데이터** → AI 학습용으로 재활용 가능

---

## 🔧 구현 목표

- 실시간 **얼굴 감지 및 마스킹 (Blur)** → 프라이버시 보호
- 실시간 **안전모 착용 여부 감지** → 산업 안전 확보

---

## 📦 데이터셋 다운로드 (Roboflow)

1. Roboflow 접속: https://universe.roboflow.com/joseph-nelson/hard-hat-workers  
2. "Download Dataset" 클릭  
3. 설정:
   - Format: `YOLOv5 PyTorch`
   - Version: 원하는 버전 선택  
4. `.zip` 파일 다운로드 후 압축 해제

---

## ⚙️ `data.yaml` 예시

```yaml
train: /path/to/hard_hat_workers/train/images
val: /path/to/hard_hat_workers/valid/images
test: /path/to/hard_hat_workers/test/images

nc: 3
names: ['head', 'helmet', 'person']  # 필요 시 5개 클래스로 수정 가능
