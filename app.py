import streamlit as st
from textwrap import dedent


# ============================================================
# 페이지 설정
# ============================================================

st.set_page_config(
    page_title="밸런스 게임",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ============================================================
# 게임 데이터
# ============================================================

GAME_DATA = {

    "food": {
        "title": "🍔 음식 밸런스",
        "description": "먹고 싶은 음식은 무엇?",
        "questions": [
            {
                "question": "평생 하나만 먹는다면?",
                "option_a": "🍗 치킨",
                "option_b": "🍕 피자"
            },
            {
                "question": "야식으로 하나만 고른다면?",
                "option_a": "🍜 라면",
                "option_b": "🍔 햄버거"
            },
            {
                "question": "둘 중 더 좋아하는 디저트는?",
                "option_a": "🍰 케이크",
                "option_b": "🍦 아이스크림"
            },
            {
                "question": "아침 식사로 하나만 고른다면?",
                "option_a": "🥐 빵",
                "option_b": "🍚 밥"
            },
            {
                "question": "매운 음식 하나만 고른다면?",
                "option_a": "🌶️ 매운 떡볶이",
                "option_b": "🔥 매운 닭발"
            },
            {
                "question": "둘 중 하나만 먹을 수 있다면?",
                "option_a": "🍣 초밥",
                "option_b": "🥩 스테이크"
            },
            {
                "question": "여름에 더 먹고 싶은 것은?",
                "option_a": "🍉 수박",
                "option_b": "🍧 팥빙수"
            },
            {
                "question": "커피를 하나만 마신다면?",
                "option_a": "🧊 아이스 아메리카노",
                "option_b": "🥛 카페라떼"
            }
        ]
    },

    "weekend": {
        "title": "🏖️ 주말에 뭐 하지?",
        "description": "주말을 보내는 가장 좋은 방법",
        "questions": [
            {
                "question": "주말에 하루 종일 한다면?",
                "option_a": "🎮 집에서 게임",
                "option_b": "🚗 드라이브"
            },
            {
                "question": "주말 아침에 일어났다면?",
                "option_a": "😴 다시 자기",
                "option_b": "🏃 바로 밖으로 나가기"
            },
            {
                "question": "친구와 주말을 보낸다면?",
                "option_a": "🍽️ 맛집 탐방",
                "option_b": "🎬 영화 보기"
            },
            {
                "question": "주말에 갑자기 시간이 생겼다면?",
                "option_a": "🏖️ 바다 가기",
                "option_b": "⛰️ 산 가기"
            },
            {
                "question": "주말 저녁에는?",
                "option_a": "🍽️ 외식하기",
                "option_b": "🏠 집에서 배달음식"
            },
            {
                "question": "주말에 혼자라면?",
                "option_a": "📚 카페에서 책 읽기",
                "option_b": "🎧 집에서 음악 듣기"
            },
            {
                "question": "주말 여행을 간다면?",
                "option_a": "🚆 기차 여행",
                "option_b": "🚗 자동차 여행"
            },
            {
                "question": "완벽한 일요일은?",
                "option_a": "☀️ 아침부터 활동하기",
                "option_b": "🛌 늦잠 자고 느긋하게 보내기"
            }
        ]
    },

    "travel": {
        "title": "✈️ 가고 싶은 여행지",
        "description": "당신의 여행 스타일은?",
        "questions": [
            {
                "question": "휴가를 떠난다면?",
                "option_a": "🏝️ 하와이",
                "option_b": "🗼 파리"
            },
            {
                "question": "둘 중 하나만 간다면?",
                "option_a": "🇯🇵 일본",
                "option_b": "🇹🇭 태국"
            },
            {
                "question": "여행 스타일은?",
                "option_a": "🏖️ 휴양 여행",
                "option_b": "🗺️ 관광 여행"
            },
            {
                "question": "겨울 여행을 간다면?",
                "option_a": "❄️ 스키장",
                "option_b": "🌴 따뜻한 나라"
            },
            {
                "question": "유럽에서 하나만 간다면?",
                "option_a": "🇫🇷 프랑스",
                "option_b": "🇮🇹 이탈리아"
            },
            {
                "question": "여행할 때 더 중요한 것은?",
                "option_a": "🍽️ 맛있는 음식",
                "option_b": "📸 멋진 풍경"
            },
            {
                "question": "여행에서 숙소를 고른다면?",
                "option_a": "🏨 고급 호텔",
                "option_b": "🏡 감성 숙소"
            },
            {
                "question": "갑자기 3일 휴가가 생겼다면?",
                "option_a": "✈️ 해외여행",
                "option_b": "🚗 국내여행"
            }
        ]
    }
}


# ============================================================
# CSS
# ============================================================

st.markdown(
    dedent(
        """
        <style>

        /* -----------------------------------------
           전체 페이지
        ----------------------------------------- */

        .stApp {
            background:
                radial-gradient(
                    circle at 15% 10%,
                    #f5ecff 0%,
                    #ffffff 38%,
                    #eef3ff 100%
                );
        }

        .block-container {
            max-width: 900px !important;
            padding-top: 25px !important;
            padding-bottom: 50px !important;
        }


        /* -----------------------------------------
           제목
        ----------------------------------------- */

        .main-title {
            text-align: center;
            color: #111827;
            font-size: 48px;
            font-weight: 900;
            letter-spacing: -2px;
            margin-bottom: 5px;
        }

        .main-subtitle {
            text-align: center;
            color: #6b7280;
            font-size: 16px;
            margin-bottom: 28px;
        }


        /* -----------------------------------------
           카테고리
        ----------------------------------------- */

        .category-card {
            background: rgba(255,255,255,0.92);
            border: 1px solid rgba(255,255,255,0.9);
            border-radius: 25px;
            padding: 30px 20px;
            text-align: center;
            min-height: 190px;
            box-shadow:
                0 12px 35px rgba(31, 41, 55, 0.08);
        }

        .category-icon {
            font-size: 52px;
            line-height: 1.2;
            margin-bottom: 12px;
        }

        .category-title {
            color: #111827;
            font-size: 22px;
            font-weight: 900;
        }

        .category-description {
            color: #6b7280;
            font-size: 14px;
            margin-top: 8px;
        }


        /* -----------------------------------------
           진행률
        ----------------------------------------- */

        .progress-text {
            text-align: center;
            color: #6b7280;
            font-size: 14px;
            margin-top: 8px;
            margin-bottom: 18px;
        }


        /* -----------------------------------------
           질문 카드
        ----------------------------------------- */

        .question-card {
            background: rgba(255,255,255,0.97);
            border-radius: 30px;
            padding: 38px 25px;
            text-align: center;
            box-shadow:
                0 18px 50px rgba(31, 41, 55, 0.10);
            border: 1px solid rgba(255,255,255,0.9);
            margin-top: 15px;
            margin-bottom: 25px;
        }

        .question-number {
            color: #8b5cf6;
            font-size: 14px;
            font-weight: 900;
            letter-spacing: 1px;
            margin-bottom: 16px;
        }

        .question-title {
            color: #111827;
            font-size: 29px;
            line-height: 1.45;
            font-weight: 900;
        }


        /* -----------------------------------------
           A / B 영역
        ----------------------------------------- */

        .choice-label {
            text-align: center;
            margin-bottom: 10px;
        }

        .choice-badge {
            display: inline-block;
            background: linear-gradient(
                135deg,
                #ff4d8d,
                #ec4899
            );
            color: white;
            font-size: 20px;
            font-weight: 900;
            padding: 5px 13px;
            border-radius: 7px;
            box-shadow:
                0 5px 15px rgba(236,72,153,0.25);
        }


        /* -----------------------------------------
           Streamlit 버튼
        ----------------------------------------- */

        div.stButton > button {
            width: 100% !important;
            min-height: 68px !important;

            border-radius: 20px !important;

            border: 2px solid #f3f4f6 !important;

            background: rgba(255,255,255,0.96) !important;

            color: #111827 !important;

            font-size: 18px !important;
            font-weight: 800 !important;

            box-shadow:
                0 10px 25px rgba(31,41,55,0.07) !important;

            transition:
                transform 0.15s ease,
                box-shadow 0.15s ease,
                border-color 0.15s ease !important;
        }

        div.stButton > button:hover {
            transform: translateY(-3px) !important;

            border-color: #c4b5fd !important;

            color: #7c3aed !important;

            box-shadow:
                0 14px 30px rgba(124,58,237,0.15) !important;
        }


        /* -----------------------------------------
           처음으로 버튼
        ----------------------------------------- */

        .home-button div.stButton > button {
            min-height: 48px !important;
            font-size: 14px !important;
        }


        /* -----------------------------------------
           결과
        ----------------------------------------- */

        .result-card {
            background:
                linear-gradient(
                    135deg,
                    #7c3aed 0%,
                    #a855f7 45%,
                    #ec4899 100%
                );

            color: white;

            border-radius: 32px;

            padding: 50px 25px;

            text-align: center;

            box-shadow:
                0 20px 50px rgba(124,58,237,0.28);

            margin-top: 25px;
        }

        .result-icon {
            font-size: 70px;
            line-height: 1;
        }

        .result-title {
            font-size: 34px;
            font-weight: 900;
            margin-top: 18px;
        }

        .result-description {
            font-size: 16px;
            margin-top: 12px;
            opacity: 0.95;
        }

        .result-score {
            font-size: 23px;
            font-weight: 800;
            margin-top: 25px;
        }


        /* -----------------------------------------
           모바일
        ----------------------------------------- */

        @media (max-width: 700px) {

            .block-container {
                padding-left: 15px !important;
                padding-right: 15px !important;
            }

            .main-title {
                font-size: 36px;
            }

            .main-subtitle {
                font-size: 14px;
            }

            .question-card {
                padding: 30px 18px;
            }

            .question-title {
                font-size: 23px;
            }

            .category-card {
                min-height: 160px;
                padding: 22px 12px;
            }

            .category-icon {
                font-size: 42px;
            }

            .category-title {
                font-size: 18px;
            }

            div.stButton > button {
                font-size: 16px !important;
                min-height: 62px !important;
            }

            .result-title {
                font-size: 28px;
            }
        }

        </style>
        """
    ),
    unsafe_allow_html=True
)


# ============================================================
# Session State 초기화
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "category" not in st.session_state:
    st.session_state.category = None

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "score_a" not in st.session_state:
    st.session_state.score_a = 0

if "score_b" not in st.session_state:
    st.session_state.score_b = 0


# ============================================================
# 게임 시작
# ============================================================

def start_game(category):

    st.session_state.page = "game"

    st.session_state.category = category

    st.session_state.question_index = 0

    st.session_state.score_a = 0
    st.session_state.score_b = 0


# ============================================================
# 게임 초기화
# ============================================================

def reset_game():

    st.session_state.page = "home"

    st.session_state.category = None

    st.session_state.question_index = 0

    st.session_state.score_a = 0
    st.session_state.score_b = 0


# ============================================================
# 답변 선택
# ============================================================

def select_answer(answer):

    if answer == "A":
        st.session_state.score_a += 1

    elif answer == "B":
        st.session_state.score_b += 1

    st.session_state.question_index += 1

    category = st.session_state.category

    total_questions = len(
        GAME_DATA[category]["questions"]
    )

    if st.session_state.question_index >= total_questions:

        st.session_state.page = "result"


# ============================================================
# HOME 화면
# ============================================================

def show_home():

    st.markdown(
        '<div class="main-title">⚖️ 밸런스 게임</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        '둘 중 하나만 선택할 수 있다면 당신의 선택은?'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("### 🎮 게임을 선택하세요")

    categories = [
        (
            "food",
            "🍔",
            "음식 밸런스",
            "먹고 싶은 음식은 무엇?"
        ),
        (
            "weekend",
            "🏖️",
            "주말에 뭐 하지?",
            "주말을 보내는 가장 좋은 방법"
        ),
        (
            "travel",
            "✈️",
            "가고 싶은 여행지",
            "당신의 여행 스타일은?"
        )
    ]

    col1, col2, col3 = st.columns(3)

    columns = [col1, col2, col3]

    for column, category in zip(columns, categories):

        key = category[0]
        icon = category[1]
        title = category[2]
        description = category[3]

        with column:

            html = dedent(
                f"""
                <div class="category-card">
                    <div class="category-icon">{icon}</div>
                    <div class="category-title">{title}</div>
                    <div class="category-description">
                        {description}
                    </div>
                </div>
                """
            )

            st.markdown(
                html,
                unsafe_allow_html=True
            )

            st.write("")

            if st.button(
                "게임 시작 →",
                key=f"start_{key}"
            ):

                start_game(key)

                st.rerun()


# ============================================================
# GAME 화면
# ============================================================

def show_game():

    category = st.session_state.category

    game = GAME_DATA[category]

    questions = game["questions"]

    current_index = st.session_state.question_index

    total = len(questions)

    # 혹시 범위를 넘어갔을 경우
    if current_index >= total:

        st.session_state.page = "result"

        st.rerun()

    question = questions[current_index]

    # -----------------------------------------
    # 제목
    # -----------------------------------------

    st.markdown(
        '<div class="main-title">⚖️ 밸런스 게임</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="main-subtitle">
            {game["title"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------
    # 진행률
    # -----------------------------------------

    progress = current_index / total

    st.progress(progress)

    st.markdown(
        f"""
        <div class="progress-text">
            {current_index + 1} / {total}
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------
    # 질문 카드
    # -----------------------------------------

    question_html = dedent(
        f"""
        <div class="question-card">

            <div class="question-number">
                QUESTION {current_index + 1}
            </div>

            <div class="question-title">
                {question["question"]}
            </div>

        </div>
        """
    )

    st.markdown(
        question_html,
        unsafe_allow_html=True
    )

    # -----------------------------------------
    # 선택지
    # -----------------------------------------

    col_a, col_b = st.columns(
        2,
        gap="large"
    )

    # -----------------------------------------
    # A
    # -----------------------------------------

    with col_a:

        st.markdown(
            """
            <div class="choice-label">
                <span class="choice-badge">A</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            question["option_a"],
            key=f"answer_a_{current_index}"
        ):

            select_answer("A")

            st.rerun()

    # -----------------------------------------
    # B
    # -----------------------------------------

    with col_b:

        st.markdown(
            """
            <div class="choice-label">
                <span class="choice-badge">B</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            question["option_b"],
            key=f"answer_b_{current_index}"
        ):

            select_answer("B")

            st.rerun()

    # -----------------------------------------
    # 처음으로
    # -----------------------------------------

    st.write("")

    st.markdown(
        '<div class="home-button">',
        unsafe_allow_html=True
    )

    if st.button(
        "🏠 처음으로",
        key=f"home_{current_index}"
    ):

        reset_game()

        st.rerun()

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# RESULT 화면
# ============================================================

def show_result():

    category = st.session_state.category

    game = GAME_DATA[category]

    score_a = st.session_state.score_a
    score_b = st.session_state.score_b

    total = score_a + score_b

    # -----------------------------------------
    # 결과 판정
    # -----------------------------------------

    if score_a > score_b:

        icon = "🅰️"
        title = "당신은 A 선택파!"
        description = "당신은 확실한 A 취향을 가지고 있네요."

    elif score_b > score_a:

        icon = "🅱️"
        title = "당신은 B 선택파!"
        description = "당신은 확실한 B 취향을 가지고 있네요."

    else:

        icon = "⚖️"
        title = "완벽한 밸런스!"
        description = "A와 B를 똑같이 좋아하는군요."

    # -----------------------------------------
    # 제목
    # -----------------------------------------

    st.markdown(
        '<div class="main-title">🎉 게임 종료!</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="main-subtitle">
            {game["title"]} 결과
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------
    # 결과 카드
    # -----------------------------------------

    result_html = dedent(
        f"""
        <div class="result-card">

            <div class="result-icon">
                {icon}
            </div>

            <div class="result-title">
                {title}
            </div>

            <div class="result-description">
                {description}
            </div>

            <div class="result-score">
                A {score_a} : {score_b} B
            </div>

        </div>
        """
    )

    st.markdown(
        result_html,
        unsafe_allow_html=True
    )

    # -----------------------------------------
    # 퍼센트
    # -----------------------------------------

    if total > 0:

        percent_a = round(
            score_a / total * 100
        )

        percent_b = round(
            score_b / total * 100
        )

        st.write("")

        st.markdown(
            f"""
            <div style="
                text-align:center;
                color:#6b7280;
                font-size:16px;
                margin:15px 0 25px 0;
            ">
                A {percent_a}% &nbsp; · &nbsp; B {percent_b}%
            </div>
            """,
            unsafe_allow_html=True
        )

    # -----------------------------------------
    # 버튼
    # -----------------------------------------

    col1, col2 = st.columns(
        2,
        gap="large"
    )

    with col1:

        if st.button(
            "🔄 다시 하기",
            key="restart_game"
        ):

            st.session_state.question_index = 0

            st.session_state.score_a = 0
            st.session_state.score_b = 0

            st.session_state.page = "game"

            st.rerun()

    with col2:

        if st.button(
            "🏠 다른 게임",
            key="other_game"
        ):

            reset_game()

            st.rerun()


# ============================================================
# 메인 실행
# ============================================================

if st.session_state.page == "home":

    show_home()

elif st.session_state.page == "game":

    show_game()

elif st.session_state.page == "result":

    show_result()
