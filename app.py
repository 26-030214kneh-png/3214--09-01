import streamlit as st
import json
import random

# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="밸런스 게임",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>

    /* 전체 배경 */
    .stApp {
        background:
            radial-gradient(
                circle at top left,
                #f3e8ff 0%,
                #ffffff 35%,
                #eef2ff 100%
            );
    }

    /* 기본 여백 */
    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* 제목 */
    .main-title {
        text-align: center;
        font-size: 46px;
        font-weight: 900;
        color: #111827;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        color: #6b7280;
        font-size: 17px;
        margin-bottom: 30px;
    }

    /* 카테고리 카드 */
    .category-card {
        background: rgba(255,255,255,0.85);
        border-radius: 24px;
        padding: 28px 20px;
        text-align: center;
        box-shadow: 0 10px 35px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.8);
        min-height: 190px;
    }

    .category-icon {
        font-size: 50px;
        margin-bottom: 8px;
    }

    .category-title {
        font-size: 23px;
        font-weight: 800;
        color: #111827;
    }

    .category-description {
        color: #6b7280;
        font-size: 14px;
        margin-top: 8px;
    }

    /* 게임 카드 */
    .question-card {
        background: rgba(255,255,255,0.95);
        border-radius: 28px;
        padding: 32px 25px;
        box-shadow: 0 15px 45px rgba(0,0,0,0.10);
        text-align: center;
        margin-bottom: 20px;
    }

    .question-number {
        color: #7c3aed;
        font-size: 14px;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .question-title {
        font-size: 27px;
        font-weight: 800;
        color: #111827;
        line-height: 1.4;
    }

    /* VS */
    .vs {
        text-align: center;
        font-size: 26px;
        font-weight: 900;
        color: #ef4444;
        margin: 12px 0;
    }

    /* 결과 */
    .result-card {
        background: linear-gradient(
            135deg,
            #7c3aed,
            #ec4899
        );
        color: white;
        border-radius: 30px;
        padding: 45px 25px;
        text-align: center;
        box-shadow: 0 20px 50px rgba(124,58,237,0.25);
    }

    .result-icon {
        font-size: 70px;
    }

    .result-title {
        font-size: 35px;
        font-weight: 900;
        margin-top: 10px;
    }

    .result-score {
        font-size: 20px;
        margin-top: 15px;
    }

    /* 버튼 */
    div.stButton > button {
        width: 100%;
        border-radius: 18px;
        min-height: 65px;
        font-size: 19px;
        font-weight: 800;
        border: none;
        background: white;
        color: #111827;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-3px);
        border-color: #7c3aed;
        color: #7c3aed;
        box-shadow: 0 12px 30px rgba(124,58,237,0.15);
    }

    /* 모바일 */
    @media (max-width: 600px) {

        .main-title {
            font-size: 34px;
        }

        .sub-title {
            font-size: 14px;
        }

        .question-title {
            font-size: 22px;
        }

        .block-container {
            padding-left: 15px;
            padding-right: 15px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 데이터 불러오기
# =========================================================

@st.cache_data
def load_questions():
    with open("questions.json", "r", encoding="utf-8") as f:
        return json.load(f)


questions = load_questions()


# =========================================================
# Session State
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "category" not in st.session_state:
    st.session_state.category = None

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score_a" not in st.session_state:
    st.session_state.score_a = 0

if "score_b" not in st.session_state:
    st.session_state.score_b = 0

if "answers" not in st.session_state:
    st.session_state.answers = []


# =========================================================
# 게임 시작
# =========================================================

def start_game(category):

    st.session_state.category = category
    st.session_state.current_question = 0
    st.session_state.score_a = 0
    st.session_state.score_b = 0
    st.session_state.answers = []

    st.session_state.page = "game"


# =========================================================
# 선택 처리
# =========================================================

def choose_answer(answer):

    if answer == "A":
        st.session_state.score_a += 1
    else:
        st.session_state.score_b += 1

    st.session_state.answers.append(answer)

    st.session_state.current_question += 1

    category_questions = questions[
        st.session_state.category
    ]

    if (
        st.session_state.current_question
        >= len(category_questions)
    ):
        st.session_state.page = "result"


# =========================================================
# 게임 초기화
# =========================================================

def reset_game():

    st.session_state.page = "home"
    st.session_state.category = None
    st.session_state.current_question = 0
    st.session_state.score_a = 0
    st.session_state.score_b = 0
    st.session_state.answers = []


# =========================================================
# HOME
# =========================================================

def home_page():

    st.markdown(
        '<div class="main-title">⚖️ 밸런스 게임</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        '둘 중 하나만 선택할 수 있다면 당신의 선택은?'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("### 🎮 게임 선택")

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

    cols = st.columns(3)

    for i, category in enumerate(categories):

        key = category[0]
        icon = category[1]
        title = category[2]
        description = category[3]

        with cols[i]:

            st.markdown(
                f"""
                <div class="category-card">
                    <div class="category-icon">{icon}</div>
                    <div class="category-title">
                        {title}
                    </div>
                    <div class="category-description">
                        {description}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")

            if st.button(
                "게임 시작 →",
                key=f"start_{key}"
            ):
                start_game(key)
                st.rerun()


# =========================================================
# GAME
# =========================================================

def game_page():

    category = st.session_state.category

    category_questions = questions[category]

    current = st.session_state.current_question

    # 안전 처리
    if current >= len(category_questions):
        st.session_state.page = "result"
        st.rerun()

    question = category_questions[current]

    total = len(category_questions)

    # 상단
    st.markdown(
        '<div class="main-title">⚖️ 밸런스 게임</div>',
        unsafe_allow_html=True
    )

    # 진행률
    progress = current / total

    st.progress(progress)

    st.markdown(
        f"""
        <div style="
            text-align:center;
            color:#6b7280;
            margin:10px 0 20px 0;
        ">
            {current + 1} / {total}
        </div>
        """,
        unsafe_allow_html=True
    )

    # 질문
    st.markdown(
        f"""
        <div class="question-card">

            <div class="question-number">
                QUESTION {current + 1}
            </div>

            <div class="question-title">
                {question["question"]}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # 선택지
    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div style="
                text-align:center;
                font-size:30px;
                margin-bottom:10px;
            ">
                🅰️
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            question["option_a"],
            key=f"a_{current}"
        ):
            choose_answer("A")
            st.rerun()

    with col2:

        st.markdown(
            """
            <div style="
                text-align:center;
                font-size:30px;
                margin-bottom:10px;
            ">
                🅱️
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            question["option_b"],
            key=f"b_{current}"
        ):
            choose_answer("B")
            st.rerun()

    st.write("")

    if st.button(
        "🏠 처음으로",
        key="game_home"
    ):
        reset_game()
        st.rerun()


# =========================================================
# RESULT
# =========================================================

def result_page():

    category = st.session_state.category

    score_a = st.session_state.score_a
    score_b = st.session_state.score_b

    total = score_a + score_b

    if score_a > score_b:
        winner = "A"
    elif score_b > score_a:
        winner = "B"
    else:
        winner = "DRAW"

    if winner == "A":

        result_title = "당신은 A 선택파!"
        result_description = "당신은 확실한 A 취향을 가지고 있네요."
        result_icon = "🅰️"

    elif winner == "B":

        result_title = "당신은 B 선택파!"
        result_description = "당신은 확실한 B 취향을 가지고 있네요."
        result_icon = "🅱️"

    else:

        result_title = "완벽한 밸런스!"
        result_description = "A와 B를 똑같이 좋아하는군요."
        result_icon = "⚖️"

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#6b7280;
            margin-bottom:20px;
        ">
            GAME RESULT
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="result-card">

            <div class="result-icon">
                {result_icon}
            </div>

            <div class="result-title">
                {result_title}
            </div>

            <div style="
                font-size:17px;
                margin-top:12px;
            ">
                {result_description}
            </div>

            <div class="result-score">
                A {score_a} : {score_b} B
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if total > 0:

        a_percent = round(
            score_a / total * 100
        )

        b_percent = round(
            score_b / total * 100
        )

        st.markdown(
            f"""
            <div style="
                text-align:center;
                color:#6b7280;
                margin:20px 0;
            ">
                A {a_percent}% · B {b_percent}%
            </div>
            """,
            unsafe_allow_html=True
        )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🔄 다시 하기",
            key="restart"
        ):

            st.session_state.current_question = 0
            st.session_state.score_a = 0
            st.session_state.score_b = 0
            st.session_state.answers = []
            st.session_state.page = "game"

            st.rerun()

    with col2:

        if st.button(
            "🏠 다른 게임",
            key="other_game"
        ):

            reset_game()
            st.rerun()


# =========================================================
# 페이지 실행
# =========================================================

if st.session_state.page == "home":

    home_page()

elif st.session_state.page == "game":

    game_page()

elif st.session_state.page == "result":

    result_page()
