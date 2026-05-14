import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 진로 추천기",
    page_icon="🌈",
    layout="centered"
)

st.title("🌈 MBTI 진로 추천기")
st.markdown("### 💡 나한테 어울리는 직업은 뭘까?")
st.write("MBTI를 선택하면 ✨ 어울리는 진로 2개를 추천해줄게!")

# MBTI 데이터
career_data = {
    "INTJ": [
        {
            "job": "🧠 데이터 사이언티스트",
            "major": "컴퓨터공학과, 통계학과",
            "personality": "논리적이고 분석하는 걸 좋아하는 사람!"
        },
        {
            "job": "🏗️ 건축가",
            "major": "건축학과",
            "personality": "계획 세우기 좋아하고 창의적인 사람!"
        }
    ],
    "INTP": [
        {
            "job": "💻 프로그래머",
            "major": "소프트웨어학과, 컴퓨터공학과",
            "personality": "호기심 많고 문제 해결을 좋아하는 사람!"
        },
        {
            "job": "🔬 연구원",
            "major": "물리학과, 화학과",
            "personality": "새로운 지식을 탐구하는 걸 좋아하는 사람!"
        }
    ],
    "ENTJ": [
        {
            "job": "📈 CEO",
            "major": "경영학과",
            "personality": "리더십 있고 목표지향적인 사람!"
        },
        {
            "job": "⚖️ 변호사",
            "major": "법학과",
            "personality": "논리적으로 말 잘하고 추진력 있는 사람!"
        }
    ],
    "ENTP": [
        {
            "job": "🎤 마케터",
            "major": "광고홍보학과",
            "personality": "아이디어 많고 말하는 걸 좋아하는 사람!"
        },
        {
            "job": "🚀 스타트업 창업가",
            "major": "경영학과",
            "personality": "도전정신 강하고 창의적인 사람!"
        }
    ],
    "INFJ": [
        {
            "job": "💖 상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어나고 따뜻한 사람!"
        },
        {
            "job": "✍️ 작가",
            "major": "문예창작과",
            "personality": "감수성이 풍부하고 상상력이 좋은 사람!"
        }
    ],
    "INFP": [
        {
            "job": "🎨 일러스트레이터",
            "major": "디자인학과",
            "personality": "감성적이고 창의력이 풍부한 사람!"
        },
        {
            "job": "🎬 영화감독",
            "major": "영화영상학과",
            "personality": "자기 표현을 좋아하는 사람!"
        }
    ],
    "ENFJ": [
        {
            "job": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "사람들을 이끄는 걸 좋아하는 사람!"
        },
        {
            "job": "🌍 사회복지사",
            "major": "사회복지학과",
            "personality": "배려심 많고 책임감 있는 사람!"
        }
    ],
    "ENFP": [
        {
            "job": "📺 유튜버",
            "major": "미디어커뮤니케이션학과",
            "personality": "에너지 넘치고 사람들과 소통하는 걸 좋아하는 사람!"
        },
        {
            "job": "🎭 배우",
            "major": "연극영화과",
            "personality": "표현력이 풍부하고 자유로운 사람!"
        }
    ],
    "ISTJ": [
        {
            "job": "🏦 회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 책임감 강한 사람!"
        },
        {
            "job": "👮 경찰관",
            "major": "경찰행정학과",
            "personality": "원칙을 중요하게 생각하는 사람!"
        }
    ],
    "ISFJ": [
        {
            "job": "💉 간호사",
            "major": "간호학과",
            "personality": "세심하고 배려심 깊은 사람!"
        },
        {
            "job": "🏥 물리치료사",
            "major": "물리치료학과",
            "personality": "다른 사람을 돕는 걸 좋아하는 사람!"
        }
    ],
    "ESTJ": [
        {
            "job": "📊 공무원",
            "major": "행정학과",
            "personality": "체계적이고 리더십 있는 사람!"
        },
        {
            "job": "🏢 관리자",
            "major": "경영학과",
            "personality": "조직 관리에 능숙한 사람!"
        }
    ],
    "ESFJ": [
        {
            "job": "🩺 치위생사",
            "major": "치위생학과",
            "personality": "친절하고 사람 챙기는 걸 좋아하는 사람!"
        },
        {
            "job": "🎉 행사기획자",
            "major": "호텔관광학과",
            "personality": "사람들과 함께 일하는 걸 좋아하는 사람!"
        }
    ],
    "ISTP": [
        {
            "job": "🔧 엔지니어",
            "major": "기계공학과",
            "personality": "손으로 만드는 걸 좋아하는 사람!"
        },
        {
            "job": "🚗 자동차 디자이너",
            "major": "자동차공학과",
            "personality": "실용적이고 관찰력이 좋은 사람!"
        }
    ],
    "ISFP": [
        {
            "job": "📸 사진작가",
            "major": "사진영상학과",
            "personality": "감각적이고 자유로운 사람!"
        },
        {
            "job": "💄 메이크업 아티스트",
            "major": "뷰티미용학과",
            "personality": "예술 감각이 뛰어난 사람!"
        }
    ],
    "ESTP": [
        {
            "job": "⚽ 스포츠 코치",
            "major": "체육학과",
            "personality": "활동적이고 에너지 넘치는 사람!"
        },
        {
            "job": "🛫 승무원",
            "major": "항공서비스학과",
            "personality": "사교적이고 순발력 있는 사람!"
        }
    ],
    "ESFP": [
        {
            "job": "🎤 방송인",
            "major": "방송연예과",
            "personality": "밝고 사람들의 관심을 즐기는 사람!"
        },
        {
            "job": "🍰 파티셰",
            "major": "제과제빵학과",
            "personality": "감각적이고 손재주 좋은 사람!"
        }
    ]
}

mbti_list = list(career_data.keys())

selected_mbti = st.selectbox(
    "🧐 너의 MBTI를 선택해봐!",
    mbti_list
)

if st.button("✨ 진로 추천 받기"):
    st.success(f"{selected_mbti} 유형에게 어울리는 진로를 알려줄게!")

    careers = career_data[selected_mbti]

    for career in careers:
        st.markdown("---")
        st.subheader(career["job"])
        st.write(f"🎓 추천 학과: {career['major']}")
        st.write(f"🌟 어울리는 성격: {career['personality']}")

    st.balloons()

st.markdown("---")
st.caption("💖 MBTI는 참고용일 뿐! 가장 중요한 건 네가 좋아하는 일이야 😎")
