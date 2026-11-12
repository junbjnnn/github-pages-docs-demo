// Hiển thị thời điểm trang được tải để chứng minh JS từ docs/js/ được serve đúng.
document.addEventListener("DOMContentLoaded", () => {
  const el = document.getElementById("loaded-at");
  if (el) el.textContent = new Date().toLocaleString();
});
