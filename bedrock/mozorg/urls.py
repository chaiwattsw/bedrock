# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from django.conf import settings
from django.urls import path

from bedrock.redirects.util import redirect

from . import views
from .dev_urls import urlpatterns as dev_only_urlpatterns
from .util import page

urlpatterns = (
    path("", views.home_view, name="mozorg.home"),
    page("about/", "mozorg/about/index.html", ftl_files=["mozorg/about"]),
    page("about/manifesto/", "mozorg/about/manifesto.html", ftl_files=["mozorg/about/manifesto"]),
    page("about/manifesto/details/", "mozorg/about/manifesto-details.html", ftl_files=["mozorg/about/manifesto"]),
    page("about/leadership/", "mozorg/about/leadership.html"),
    page("about/policy/lean-data/", "mozorg/about/policy/lean-data/index.html"),
    page("about/policy/lean-data/build-security/", "mozorg/about/policy/lean-data/build-security.html"),
    page("about/policy/lean-data/stay-lean/", "mozorg/about/policy/lean-data/stay-lean.html"),
    page("about/policy/lean-data/engage-users/", "mozorg/about/policy/lean-data/engage-users.html"),
    page("about/policy/patents/", "mozorg/about/policy/patents/index.html"),
    page("about/policy/patents/license/", "mozorg/about/policy/patents/license.html"),
    page("about/policy/patents/license/1.0/", "mozorg/about/policy/patents/license-1.0.html"),
    page("about/policy/patents/guide/", "mozorg/about/policy/patents/guide.html"),
    page("about/this-site/", "mozorg/about/this-site.html", ftl_files=["mozorg/about/this-site.ftl"]),
    page("book/", "mozorg/book.html"),
    path("credits/", views.credits_view, name="mozorg.credits"),
    page("credits/faq/", "mozorg/credits-faq.html"),
    page("about/history/", "mozorg/about/history.html", ftl_files=["mozorg/about/history"]),
    # Bug 981063, catch all for old calendar urls.
    # must be here to avoid overriding the above
    redirect(r"^projects/calendar/", "https://www.thunderbird.net/calendar/", locale_prefix=False),
    page("mission/", "mozorg/mission.html", ftl_files=["mozorg/mission"]),
    path("about/forums/", views.forums_view, name="mozorg.about.forums.forums"),
    page("about/forums/etiquette/", "mozorg/about/forums/etiquette.html"),
    page("about/forums/cancellation/", "mozorg/about/forums/cancellation.html"),
    page("about/governance/", "mozorg/about/governance/governance.html"),
    page("about/governance/roles/", "mozorg/about/governance/roles.html"),
    page("about/governance/policies/", "mozorg/about/governance/policies/policies.html"),
    page("about/governance/policies/commit/", "mozorg/about/governance/policies/commit.html"),
    page("about/governance/policies/commit/access-policy/", "mozorg/about/governance/policies/commit/access-policy.html"),
    page("about/governance/policies/commit/requirements/", "mozorg/about/governance/policies/commit/requirements.html"),
    page("about/governance/policies/security-group/bugs/", "mozorg/about/governance/policies/security/bugs.html"),
    page("about/governance/policies/security-group/membership/", "mozorg/about/governance/policies/security/membership.html"),
    page("about/governance/policies/security-group/certs/policy/", "mozorg/about/governance/policies/security/certs/policy.html"),
    page("about/governance/organizations/", "mozorg/about/governance/organizations.html"),
    page(
        "about/governance/policies/participation/reporting/",
        "mozorg/about/governance/policies/reporting.html",
        ftl_files=["mozorg/about/governance/policies/reporting"],
    ),
    page(
        "about/governance/policies/participation/",
        "mozorg/about/governance/policies/participation.html",
        ftl_files=["mozorg/about/governance/policies/participation"],
    ),
    page(
        "about/governance/policies/participation/reporting/community-hotline/",
        "mozorg/about/governance/policies/community-hotline.html",
        ftl_files=["mozorg/about/governance/policies/community-hotline"],
    ),
    page("about/governance/policies/module-ownership/", "mozorg/about/governance/policies/module-ownership.html"),
    page("about/governance/policies/regressions/", "mozorg/about/governance/policies/regressions.html"),
    page("about/policy/transparency/", "mozorg/about/policy/transparency/index.html"),
    page("about/policy/transparency/jan-dec-2015/", "mozorg/about/policy/transparency/jan-dec-2015.html"),
    page("about/policy/transparency/jan-jun-2016/", "mozorg/about/policy/transparency/jan-jun-2016.html"),
    page("about/policy/transparency/jul-dec-2016/", "mozorg/about/policy/transparency/jul-dec-2016.html"),
    page("about/policy/transparency/jan-jun-2017/", "mozorg/about/policy/transparency/jan-jun-2017.html"),
    page("about/policy/transparency/jul-dec-2017/", "mozorg/about/policy/transparency/jul-dec-2017.html"),
    page("about/policy/transparency/jan-jun-2018/", "mozorg/about/policy/transparency/jan-jun-2018.html"),
    page("about/policy/transparency/jul-dec-2018/", "mozorg/about/policy/transparency/jul-dec-2018.html"),
    page("about/policy/transparency/jan-jun-2019/", "mozorg/about/policy/transparency/jan-jun-2019.html"),
    page("about/policy/transparency/jul-dec-2019/", "mozorg/about/policy/transparency/jul-dec-2019.html"),
    page("about/policy/transparency/jan-jun-2020/", "mozorg/about/policy/transparency/jan-jun-2020.html"),
    page("about/policy/transparency/jul-dec-2020/", "mozorg/about/policy/transparency/jul-dec-2020.html"),
    page("about/policy/transparency/jan-jun-2021/", "mozorg/about/policy/transparency/jan-jun-2021.html"),
    page("about/policy/transparency/jul-dec-2021/", "mozorg/about/policy/transparency/jul-dec-2021.html"),
    page("contact/", "mozorg/contact/contact-landing.html"),
    page("contact/spaces/", "mozorg/contact/spaces/spaces-landing.html"),
    page("contact/spaces/beijing/", "mozorg/contact/spaces/beijing.html"),
    page("contact/spaces/berlin/", "mozorg/contact/spaces/berlin.html"),
    page("contact/spaces/paris/", "mozorg/contact/spaces/paris.html"),
    page("contact/spaces/portland/", "mozorg/contact/spaces/portland.html"),
    page("contact/spaces/san-francisco/", "mozorg/contact/spaces/san-francisco.html"),
    page("contact/spaces/toronto/", "mozorg/contact/spaces/toronto.html"),
    page("MPL/", "mozorg/mpl/index.html"),
    page("MPL/historical/", "mozorg/mpl/historical.html"),
    page("MPL/license-policy/", "mozorg/mpl/license-policy.html"),
    page("MPL/headers/", "mozorg/mpl/headers/index.html"),
    page("MPL/1.1/", "mozorg/mpl/1.1/index.html"),
    page("MPL/1.1/FAQ/", "mozorg/mpl/1.1/faq.html"),
    page("MPL/1.1/annotated/", "mozorg/mpl/1.1/annotated/index.html"),
    page("MPL/2.0/", "mozorg/mpl/2.0/index.html"),
    page("MPL/2.0/FAQ/", "mozorg/mpl/2.0/faq.html"),
    page("MPL/2.0/Revision-FAQ/", "mozorg/mpl/2.0/revision-faq.html"),
    page("MPL/2.0/combining-mpl-and-gpl/", "mozorg/mpl/2.0/combining-mpl-and-gpl.html"),
    page("MPL/2.0/differences/", "mozorg/mpl/2.0/differences.html"),
    page("MPL/2.0/permissive-code-into-mpl/", "mozorg/mpl/2.0/permissive-code-into-mpl.html"),
    page("contribute/", "mozorg/contribute.html", ftl_files=["mozorg/contribute"]),
    page("moss/", "mozorg/moss/index.html"),
    page("moss/foundational-technology/", "mozorg/moss/foundational-technology.html"),
    page("moss/mission-partners/", "mozorg/moss/mission-partners.html"),
    page("moss/secure-open-source/", "mozorg/moss/secure-open-source.html"),
    path("robots.txt", views.Robots.as_view(), name="robots.txt"),
    # namespaces
    path("2004/em-rdf", views.namespaces, {"namespace": "em-rdf"}),
    path("2005/app-update", views.namespaces, {"namespace": "update"}),
    path("2006/addons-blocklist", views.namespaces, {"namespace": "addons-bl"}),
    path("2006/browser/search/", views.namespaces, {"namespace": "mozsearch"}),
    path("keymaster/gatekeeper/there.is.only.xul", views.namespaces, {"namespace": "xul"}),
    path("microsummaries/0.1", views.namespaces, {"namespace": "microsummaries"}),
    path("projects/xforms/2005/type", views.namespaces, {"namespace": "xforms-type"}),
    path("xbl", views.namespaces, {"namespace": "xbl"}),
    path("locales/", views.locales, name="mozorg.locales"),
    # Diversity and inclusion redirect
    redirect(r"^diversity/$", "mozorg.diversity.2021.index", name="diversity", locale_prefix=False),
    # Main paths
    page("diversity/2021/", "mozorg/diversity/2021/index.html"),
    page("diversity/2021/mozilla-foundation-data/", "mozorg/diversity/2021/mofo-data.html"),
    page("diversity/2021/mozilla-corporation-data/", "mozorg/diversity/2021/moco-data.html"),
    page("diversity/2021/racial-justice-commitments/", "mozorg/diversity/2021/racial-justice.html"),
    page("diversity/2021/what-we-build/", "mozorg/diversity/2021/what-we-build.html"),
    page("diversity/2021/beyond-our-products/", "mozorg/diversity/2021/beyond-products.html"),
    page("diversity/2021/who-we-are/", "mozorg/diversity/2021/who-we-are.html"),
    # Webvision
    redirect(r"^webvision/?$", "mozorg.about.webvision.summary", name="webvision", locale_prefix=False),
    path(
        "about/webvision/",
        views.WebvisionDocView.as_view(template_name="mozorg/about/webvision/summary.html", doc_name="summary"),
        name="mozorg.about.webvision.summary",
    ),
    path(
        "about/webvision/full/",
        views.WebvisionDocView.as_view(template_name="mozorg/about/webvision/full.html", doc_name="full"),
        name="mozorg.about.webvision.full",
    ),
    page("analytics-tests/", "mozorg/analytics-tests/ga-index.html"),
)

if settings.DEV:
    urlpatterns += dev_only_urlpatterns
