/**
 * 作品集页 · 原生 JS（无依赖）
 * 作用：1) 页脚年份  2) 手机端导航开关  3) 点击任意导航链接后收起菜单
 */

(function () {
  "use strict";

  // ---------- 1. 自动写入当前年份到 #year ----------
  var yearEl = document.getElementById("year");
  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  // ---------- 2. 手机端：汉堡按钮展开/收起菜单 ----------
  var toggle = document.getElementById("nav-toggle");
  var menu = document.getElementById("nav-menu");

  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    // 点击导航链接后收起菜单（含首页/作品等多页面跳转，不仅限于 # 锚点）
    var links = menu.querySelectorAll("a.nav__link");
    links.forEach(function (link) {
      link.addEventListener("click", function () {
        if (window.matchMedia("(max-width: 768px)").matches) {
          menu.classList.remove("is-open");
          toggle.setAttribute("aria-expanded", "false");
        }
      });
    });
  }
})();
