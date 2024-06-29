from .models import Product,ContactUs,Cart
from modeltranslation.translator import register, TranslationOptions

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name',)

# @register(Produc)
# class ProductTranslationOptions(TranslationOptions):
#     fields = ('name',)

@register(ContactUs)
class ContactUsTranslationOptions(TranslationOptions):
    fields = ('name',)

# @register(Cart)
# class CartTranslationOptions(TranslationOptions):
#     fields = ('product',)