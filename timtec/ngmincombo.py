from pipeline.compressors.uglifyjs import UglifyJSCompressor


class NgminComboCompressor(UglifyJSCompressor):
    def compress_js(self, js):
        ngminified = self.execute_command('ngmin', js)
        return super(NgminComboCompressor, self).compress_js(ngminified)
