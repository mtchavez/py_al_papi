task :default => :test

task :test => ["test:unit", "test:integration"]

namespace :test do
  desc "run unit tests"
  task :unit do
    sh "nosetests --with-spec --spec-color tests/unit"
  end

  desc "run integration tests"
  task :integration do
    sh "nosetests tests/integration" if false
  end
end

task :build do
  sh "python setup.py build && python setup.py install"
end

task :clean do
  rm_rf "build"
  rm_rf "dist"
  rm_f "MANIFEST"
end

namespace :pypi do
  desc "Register the package with PyPI"
  task :register => :clean do
    sh "python setup.py register"
  end

  desc "Upload a new version to PyPI"
  task :upload => :clean do
    sh "python setup.py sdist upload"
  end
end
