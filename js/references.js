(() => {
  const filterNav = document.querySelector(".ref-filters");
  if (filterNav) {
    const filterButtons = Array.from(filterNav.querySelectorAll(".ref-filter"));
    const articles = Array.from(document.querySelectorAll(".ref-item"));
    const yearGroups = Array.from(document.querySelectorAll(".ref-year"));

    filterNav.hidden = false;
    filterButtons.forEach((button) => {
      button.hidden = false;
      button.addEventListener("click", () => {
        const selected = button.dataset.filter;
        filterButtons.forEach((item) => {
          item.setAttribute("aria-pressed", String(item === button));
        });
        articles.forEach((article) => {
          article.hidden = selected !== "all" && article.dataset.sector !== selected;
        });
        yearGroups.forEach((group) => {
          group.hidden = !group.querySelector(".ref-item:not([hidden])");
        });
      });
    });
  }

  const dialog = document.querySelector(".ref-lightbox");
  if (!dialog || typeof dialog.showModal !== "function") return;

  const dialogImage = dialog.querySelector("img");
  const caption = dialog.querySelector("figcaption");
  const closeButton = dialog.querySelector(".ref-lightbox-close");
  let trigger = null;

  document.querySelectorAll(".ref-thumb").forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      trigger = link;
      const thumb = link.querySelector("img");
      dialogImage.src = link.href;
      dialogImage.width = Number(link.dataset.width);
      dialogImage.height = Number(link.dataset.height);
      dialogImage.alt = thumb.alt;
      caption.textContent = thumb.alt;
      dialog.showModal();
      closeButton.focus();
    });
  });

  closeButton.addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) dialog.close();
  });
  dialog.addEventListener("close", () => {
    if (trigger && trigger.isConnected) trigger.focus();
    trigger = null;
    dialogImage.removeAttribute("src");
    caption.textContent = "";
  });
})();
