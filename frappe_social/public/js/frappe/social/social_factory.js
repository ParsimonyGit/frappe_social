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
			'frappe_social.bundle.js'
		];

		const me = this;
		frappe.require(assets, () => {
			frappe.social.home = new frappe.social.Home({
				parent: me.make_page(true, page_name)
			});
		});
	}
};