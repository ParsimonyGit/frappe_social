frappe.views.SocialFactory = class SocialFactory extends frappe.views.Factory {
	show() {
		if (frappe.pages.social) {
			frappe.container.change_to('Social');
		} else {
			this.make('Social');
		}
	}

	make(page_name) {
		const assets = [
			'/assets/js/social.min.js'
		];

		frappe.require(assets, () => {
			frappe_social.social.home = new frappe_social.social.Home({
				parent: this.make_page(true, page_name)
			});
		});
	}
};