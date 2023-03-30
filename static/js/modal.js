//영상등록하기 버튼에 .modal-open 클래스 부여하기
const btnModalOpen = document.querySelector(".modal-open");
const modal = document.querySelector(".modal");
const btnModalClose = document.querySelector(".modal-close");
const btnSumit = document.querySelector(".btn-submit");
const body = document.querySelector("body");
const videoNameVal = document.querySelector("#video-name");
const videoDescVal = document.querySelector("#video-desc");
const videoLinkVal = document.querySelector("#video-link");

let boardId = Date.now();

function handleEvent(e) {
  e.preventDefault();
  const youTubeUrl = videoLinkVal.value.slice(
    32,
    videoLinkVal.value.length
  );
  const imgUrl = `https://i1.ytimg.com/vi/${youTubeUrl}/maxresdefault.jpg`;

  if (videoLinkVal.value == "") {
    alert("url을 입력하세요");
  } else if (!(videoLinkVal.value.substring(0, 4) == "http")) {
    alert("유효한 url형식이 아닙니다.");
  } else {
    let formData = new FormData();
    formData.append("videoname_give", videoNameVal.value);
    formData.append("videodesc_give", videoDescVal.value);
    formData.append("videolink_give", videoLinkVal.value);
    formData.append("id_give", boardId);
    formData.append("url_give", imgUrl);
    console.log(imgUrl);

    fetch("/modal", {
      headers: {
        Accept: "application / json",
      },
      method: "POST",
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => {
        window.location.reload();
      })
      .catch((error) => {
        console.log(error);
      });
  }
}

function handleModalClose() {
  modal.style.display = "none";
  body.style.overflow = "auto";
}

function handleModalOpen() {
  debugger
  modal.style.display = "block";
  body.style.overflow = "hidden";
}
btnSumit.addEventListener("click", handleEvent);
btnModalOpen.addEventListener("click", handleModalOpen);
btnModalClose.addEventListener("click", handleModalClose);