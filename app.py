import streamlit as st

# -----------------------------------
# 기본 설정
# -----------------------------------
st.set_page_config(
    page_title="🌈 MBTI 진로 & 포켓몬 추천기",
    page_icon="✨",
    layout="centered"
)

# -----------------------------------
# 제목
# -----------------------------------
st.title("🌈 MBTI 진로 & 포켓몬 추천기")
st.markdown("## 😆 나랑 닮은 직업이랑 포켓몬은 뭘까?")
st.write("MBTI를 선택하면 💼 추천 진로 + 🐾 닮은 포켓몬을 알려줄게!")

# -----------------------------------
# MBTI 데이터
# -----------------------------------
mbti_data = {

    "INTJ": {
        "careers": [
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
        "pokemon": {
            "name": "🟣 뮤츠",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
            "description": "엄청 똑똑하고 전략적인 포켓몬! 혼자 깊게 생각하는 INTJ랑 찰떡 😎"
        }
    },

    "INTP": {
        "careers": [
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
        "pokemon": {
            "name": "🧠 후딘",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
            "description": "IQ 천재 느낌의 포켓몬! 분석왕 INTP랑 완전 잘 어울려 🔍"
        }
    },

    "ENTJ": {
        "careers": [
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
        "pokemon": {
            "name": "🔥 리자몽",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
            "description": "카리스마 폭발🔥 리더 기질 넘치는 ENTJ랑 찰떡!"
        }
    },

    "ENTP": {
        "careers": [
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
        "pokemon": {
            "name": "⚡ 피카츄",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
            "description": "에너지 넘치고 장난기 가득! 분위기 메이커 ⚡"
        }
    },

    "INFJ": {
        "careers": [
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
        "pokemon": {
            "name": "🌸 가디안",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/282.png",
            "description": "상대의 마음을 이해하는 따뜻한 포켓몬 💕"
        }
    },

    "INFP": {
        "careers": [
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
        "pokemon": {
            "name": "🌙 이브이",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
            "description": "가능성이 무한한 감성 포켓몬 ✨"
        }
    },

    "ENFJ": {
        "careers": [
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
        "pokemon": {
            "name": "🦁 루카리오",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png",
            "description": "정의감 넘치고 리더 느낌 가득 😎"
        }
    },

    "ENFP": {
        "careers": [
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
        "pokemon": {
            "name": "🎈 푸린",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
            "description": "귀엽고 텐션 높은 분위기 메이커 🎶"
        }
    },

    "ISTJ": {
        "careers": [
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
        "pokemon": {
            "name": "🛡️ 거북왕",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
            "description": "든든하고 믿음직한 스타일 💪"
        }
    },

    "ISFJ": {
        "careers": [
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
        "pokemon": {
            "name": "💧 라프라스",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/131.png",
            "description": "친절하고 따뜻하게 사람들을 챙기는 포켓몬 💙"
        }
    },

    "ESTJ": {
        "careers": [
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
        "pokemon": {
            "name": "🦖 마기라스",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/248.png",
            "description": "강력하고 책임감 있는 리더 스타일 👑"
        }
    },

    "ESFJ": {
        "careers": [
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
        "pokemon": {
            "name": "🌸 해피너스",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png",
            "description": "주변 사람들을 행복하게 만드는 포켓몬 😊"
        }
    },

    "ISTP": {
        "careers": [
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
        "pokemon": {
            "name": "⚙️ 핫삼",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/212.png",
            "description": "조용하지만 실력 엄청난 냉철한 스타일 😎"
        }
    },

    "ISFP": {
        "careers": [
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
        "pokemon": {
            "name": "🍃 이상해씨",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
            "description": "차분하고 자연을 사랑하는 감성러 🌿"
        }
    },

    "ESTP": {
        "careers": [
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
        "pokemon": {
            "name": "🔥 번치코",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/257.png",
            "description": "열정 MAX! 행동파 스타일 🔥"
        }
    },

    "ESFP": {
        "careers": [
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
        ],
        "pokemon": {
            "name": "✨ 토게키스",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/468.png",
            "description": "행복 에너지 뿜뿜하는 인기쟁이 ✨"
        }
    }
}

# -----------------------------------
# MBTI 선택
# -----------------------------------
selected_mbti = st.selectbox(
    "🧐 너의 MBTI를 선택해봐!",
    list(mbti_data.keys())
)

# -----------------------------------
# 결과 버튼
# -----------------------------------
if st.button("✨ 결과 보기"):

    data = mbti_data[selected_mbti]

    st.success(f"🎉 {selected_mbti} 결과가 나왔어!")

    # -----------------------------
    # 진로 추천
    # -----------------------------
    st.markdown("## 💼 추천 진로")

    for career in data["careers"]:
        st.markdown("---")
        st.subheader(career["job"])
        st.write(f"🎓 추천 학과: {career['major']}")
        st.write(f"🌟 어울리는 성격: {career['personality']}")

    # -----------------------------
    # 포켓몬 추천
    # -----------------------------
    st.markdown("---")
    st.markdown("## 🐾 너랑 닮은 포켓몬!")

    pokemon = data["pokemon"]

    st.image(pokemon["image"], width=220)

    st.subheader(pokemon["name"])

    st.write(f"💬 {pokemon['description']}")

    st.balloons()

# -----------------------------------
# 하단 문구
# -----------------------------------
st.markdown("---")
st.caption("💖 MBTI는 재미로 보는 거야! 가장 중요한 건 네가 좋아하는 일을 찾는 것 😎")
